"""Shadowrun 5 skills with TypeSafe's Jev model.

The sr5 sheet shares its attributes with the sr6 sheet. Missing attributes are
rated first; the skills are then rated knowing them. Answers use the same 0-9
rubric as the sr6 fill and are rounded to integers.
"""

from filelock import FileLock
from typesafe_sdk import Score

from npc_creator.game_mechanics.sr5.skills import (
    EXOTIC,
    MAGICAL_KEYS,
    RESONANCE_KEYS,
    SKILL_NAMES,
)
from npc_creator.operations.jev.sr6_fill import LEVELS, build_questions as build_attribute_questions, fill_fields
from npc_creator.operations.return_types import Success

MAGICAL = "0 unless the NPC has magic (a mage, shaman, adept or other magic user). Always 0 for technomancers."
RESONANT = "0 unless the NPC is a technomancer. Hackers, deckers, riggers and everyone else without resonance have 0."
EXOTIC_NOTE = "One rating for any exotic one of these; 0 unless the NPC clearly uses something unusual."
GENERIC = "Most people have few skill points; 0 if the NPC has no use for it."


def hint(key):
    if key in MAGICAL_KEYS:
        return MAGICAL
    if key in RESONANCE_KEYS:
        return RESONANT
    if SKILL_NAMES[key] in EXOTIC:
        return EXOTIC_NOTE
    return GENERIC


def build_questions(keys) -> dict:
    return {
        key: Score(
            instructions=(
                "How skilled is the Shadowrun NPC described in `npc` in the Shadowrun 5th edition "
                f"active skill '{SKILL_NAMES[key]}'? {hint(key)}"
            ),
            criteria=LEVELS,
        )
        for key in keys
    }


class JevSr5Fill:
    def __init__(self, entity, schema: str = "sr5"):
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
        kind = self.__class__.__name__
        core = [name for name in self.entity.SCHEMAS[self.schema].model_fields if name not in SKILL_NAMES]
        missing = [name for name in core if name not in self.entity.attributes]
        if missing:
            result = fill_fields(self.entity, missing, build_attribute_questions(missing), kind)
            if not result:
                return result

        skills = [key for key in SKILL_NAMES if key not in self.entity.attributes]
        return fill_fields(self.entity, skills, build_questions(skills), kind)
