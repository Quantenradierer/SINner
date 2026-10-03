"""Attribute and skill selection with TypeSafe's Jev model.

Jev answers one ``Score`` per sr6 field on a shared 0-9 rubric. Its answers
are expected values, so they are rounded to integers.
"""

import json
import logging

from filelock import FileLock
from typesafe_sdk import Score, TypeSafeClient, TypeSafeError

from npc_creator import config
from npc_creator.models.gpt_request import GptRequest
from npc_creator.operations.jev.equipment_fill import npc_state
from npc_creator.operations.return_types import Failure, Success

LEVELS = [
    "None: no ability at all (not used for the core attributes and edge)",
    "Very low: untrained, clearly below average",
    "Low: below average, a hobbyist at best",
    "Average: ordinary person, basic training",
    "Competent: trained professional",
    "Skilled: well above average, a veteran",
    "Exceptional: the best of normal people",
    "Outstanding: top of a field, rare",
    "Elite: near the metatype's limit, legendary",
    "Superhuman: the absolute maximum",
]


# magic, resonance and skills may be 0; the core attributes and edge may not
MAY_BE_ZERO_PREFIXES = ("skill_", "magic", "resonance")


def build_questions(fields) -> dict:
    def hint(name):
        if name.startswith(MAY_BE_ZERO_PREFIXES):
            return ""
        return " This is never 0."

    return {
        name: Score(
            instructions=(
                f"How high is the Shadowrun NPC's {name.replace('_', ' ')}, "
                f"given the NPC described in `npc`?{hint(name)}"
            ),
            criteria=LEVELS,
        )
        for name in fields
    }


def npc_state_without(values: dict, fields) -> dict:
    return npc_state({k: v for k, v in values.items() if k not in fields})


class JevSr6Fill:
    def __init__(self, entity, schema: str = "sr6"):
        self.entity = entity
        self.schema = schema

    def call(self):
        lock = FileLock(f"lock-{self.entity.uuid}.lock")
        with lock:
            if self.entity.id:
                self.entity.refresh_from_db()
            if self.entity.schema_complete(self.schema):
                return Success()
            return self._fill()

    def _fill(self):
        fields = list(self.entity.SCHEMAS[self.schema].model_fields)
        state = npc_state_without(self.entity.values, fields)
        if self.entity.prompt and "prompt" not in state["npc"]:
            state["npc"]["prompt"] = self.entity.prompt
        questions = build_questions(fields)

        request = GptRequest(kind=self.__class__.__name__)
        request.input = {"state": state, "questions": fields}
        try:
            answers = TypeSafeClient(model=config.JEV_MODEL).system_one(state, questions)
        except TypeSafeError as e:
            logging.info(f"Jev Error: {e}")
            request.output = str(e)
            request.failed()
            request.save()
            return Failure("jev_raised_an_error", e)

        values = {name: round(answers.scores[name].score) for name in fields}
        request.output = json.dumps(
            {"request_id": answers.request_id, "usage": answers.usage.model_dump() if answers.usage else None, "values": values}
        )
        request.finished()
        request.save()

        self.entity.add_values(values)
        self.entity.save()
        return Success(values)
