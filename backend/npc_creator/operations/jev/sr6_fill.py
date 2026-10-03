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


NORMAL_RANGE = "Normal range is 1-6 for most metatypes; never 0."
AWAKENED = "Most NPCs are not awakened: 0 unless the NPC is a magic user."
RESONANT = "Most NPCs are not technomancers: 0 unless the NPC is a technomancer."

# what the old GPT schema told its model, as hints per field
HINTS = {
    "agility": f"{NORMAL_RANGE} Elves up to 7, trolls up to 5.",
    "reaction": f"{NORMAL_RANGE} Dwarves up to 5.",
    "strength": f"{NORMAL_RANGE} Dwarves and orks up to 8, trolls up to 9.",
    "willpower": f"{NORMAL_RANGE} Dwarves up to 7.",
    "charisma": f"{NORMAL_RANGE} Elves up to 8, orks and trolls up to 5.",
    "edge": "Humans 1-7, all other metatypes 1-6; never 0.",
    "magic": f"{AWAKENED} A character never has both magic and resonance.",
    "resonance": f"{RESONANT} A character never has both magic and resonance.",
    "skill_astral": "0 unless the NPC has magic.",
    "skill_conjuring": "0 unless the NPC has magic.",
    "skill_sorcery": "0 unless the NPC has magic.",
    "skill_enchanting": "0 unless the NPC has magic.",
    "skill_tasking": "Always 0, except for technomancers. Hackers, deckers, riggers and everyone else without resonance have 0.",
}


def hint(name):
    if name in HINTS:
        return HINTS[name]
    if name.startswith("skill_"):
        return "Most people have few skill points; 0 if the NPC has no use for it."
    return NORMAL_RANGE


def build_questions(fields) -> dict:
    return {
        name: Score(
            instructions=(
                f"How high is the Shadowrun NPC's {name.replace('_', ' ')}, "
                f"given the NPC described in `npc`? {hint(name)}"
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
