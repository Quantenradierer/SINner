"""Equipment selection with TypeSafe's Jev model.

Jev only judges fit: one ``Choice`` per slot, one ``Noul`` per pool item and a
``Score`` for how well-resourced the NPC is. Code owns the rules: who may have
a cyberdeck, the essence budget, how many items a pool keeps and which rating
variant an item gets.
"""

import json
import logging
from dataclasses import dataclass

from filelock import FileLock
from typesafe_sdk import Choice, Noul, Score, SystemOneResponse, TypeSafeClient, TypeSafeError

from npc_creator import config
from npc_creator.game_mechanics.manager import ALL_GEAR
from npc_creator.game_mechanics.reference_names import name_for
from npc_creator.models.gpt_request import GptRequest
from npc_creator.operations.jev.equipment_catalog import EquipmentCatalog, GearGroup
from npc_creator.operations.return_types import Failure, Success

# Jev's yes-probabilities for "carries item X" run low even for fitting items;
# the ranking is what's reliable, so the cut-offs sit well below 0.5.
NOUL_THRESHOLD = 0.5
GEAR_THRESHOLD = 0.25
CYBERWARE_THRESHOLD = 0.15
MAX_FIELD_GEAR = 10
MAX_SOFTWARE = 4
MAX_CYBERWARE = 6
ESSENCE_BUDGET = 5.0
DECKER_ONLY = ("cyberdeck", "cyberjack")

RESOURCE_LEVELS = [
    "Broke: wageslave, ganger or squatter, buys the cheapest gear or none",
    "Street professional: small-time runner, cop or fixer with decent everyday gear",
    "Seasoned professional: experienced runner or corporate security with quality gear",
    "Elite: top-tier corporate or legendary runner, buys the best available",
]


def _int(value) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


@dataclass
class NpcProfile:
    is_decker: bool
    is_awakened: bool

    @classmethod
    def from_values(cls, values: dict) -> "NpcProfile":
        return cls(
            is_decker=_int(values.get("skill_cracking")) > 0,
            is_awakened=_int(values.get("magic")) > 0
            or _int(values.get("resonance")) > 0,
        )


def _criteria(ids: list[str]) -> dict[str, str]:
    return {gear_id: name_for(gear_id) for gear_id in ids}


def _carry(group: GearGroup) -> Noul:
    return Noul(
        instructions=(
            "Does the Shadowrun NPC described in `npc` own and regularly carry "
            f"this item: {group.describe()}?"
        )
    )


def _implant(group: GearGroup) -> Noul:
    return Noul(
        instructions=(
            "Does the Shadowrun NPC described in `npc` have this cyberware "
            f"implanted: {group.describe()}?"
        )
    )


WEAPON_SLOTS = {
    "ranged": ("a rifle, shotgun, SMG or other long arm", "ranged"),
    "sidearm": ("a pistol or taser", "sidearms"),
    "melee": ("a melee or throwing weapon", "melee"),
}


def build_questions(catalog: EquipmentCatalog, profile: NpcProfile) -> dict:
    questions = {
        "resources": Score(
            instructions="How much money and gear access does the Shadowrun NPC described in `npc` have?",
            criteria=RESOURCE_LEVELS,
        ),
        "armor": Choice(
            instructions="Which clothing or body armor does the Shadowrun NPC described in `npc` usually wear?",
            criteria=_criteria(catalog.armor),
        ),
        "fake_sin": Noul(
            instructions="Does the Shadowrun NPC described in `npc` use a fake SIN (false identity)?"
        ),
    }
    for slot, (kind, field) in WEAPON_SLOTS.items():
        # presence is asked on its own: a "none" option loses against ~30 weapons
        questions[f"armed:{slot}"] = Noul(
            instructions=f"Does the Shadowrun NPC described in `npc` carry {kind}?"
        )
        questions[slot] = Choice(
            instructions=f"If the Shadowrun NPC described in `npc` carries {kind}, which one fits best?",
            criteria=_criteria(getattr(catalog, field)),
        )
    if profile.is_decker:
        questions["device"] = Choice(
            instructions="Which device does the Shadowrun NPC described in `npc` use for the Matrix?",
            criteria={
                "commlink": "A commlink: everyday phone and computer",
                "cyberdeck": "A cyberdeck: hacking device for deckers",
            },
        )
    for gear_id in catalog.helmets_and_shields:
        questions[f"armor:{gear_id}"] = Noul(
            instructions=f"Does the Shadowrun NPC described in `npc` carry this: {name_for(gear_id)}?"
        )
    for group in catalog.field_gear:
        questions[f"gear:{group.key}"] = _carry(group)
    if profile.is_decker:
        for group in catalog.software:
            questions[f"software:{group.key}"] = _carry(group)
    if not profile.is_awakened:
        questions["obvious_chrome"] = Noul(
            instructions="Would the Shadowrun NPC described in `npc` choose openly visible chrome over cyberlimbs that look natural?"
        )
        for group in _cyberware(catalog, profile):
            questions[f"cyberware:{group.key}"] = _implant(group)
    return questions


def _cyberware(catalog: EquipmentCatalog, profile: NpcProfile) -> list[GearGroup]:
    return [
        group
        for group in catalog.cyberware
        if profile.is_decker or not any(word in group.key for word in DECKER_ONLY)
    ]


class Selection:
    """Turns Jev's answers into gear ids; all equipment rules live here."""

    def __init__(self, catalog: EquipmentCatalog, profile: NpcProfile, answers: SystemOneResponse):
        self.catalog = catalog
        self.profile = profile
        self.answers = answers
        resources = answers.scores["resources"].score
        self.resource_fraction = resources / (len(RESOURCE_LEVELS) - 1)

    def _rated(self, variants: list[str]) -> str:
        index = round(self.resource_fraction * (len(variants) - 1))
        return variants[index]

    def _variant(self, group: GearGroup) -> str:
        if group.rated:
            return self._rated(group.variants)
        if len(group.variants) == 1:
            return group.variants[0]
        # cyberlimb: synthetic/obvious, then the right side if sided
        look = "obvious" if self.answers.nouls["obvious_chrome"].noul >= NOUL_THRESHOLD else "synthetic"
        matching = [v for v in group.variants if f"/{look}" in v]
        right = [v for v in matching if v.endswith("/right")]
        return (right or matching or group.variants)[0]

    def _weapon(self, slot: str) -> list[str]:
        if self.answers.nouls[f"armed:{slot}"].noul < NOUL_THRESHOLD:
            return []
        return [self.answers.choices[slot].choice]

    def _device(self) -> str:
        decks = self.profile.is_decker and self.answers.choices["device"].choice == "cyberdeck"
        return self._rated(self.catalog.cyberdecks if decks else self.catalog.commlinks)

    def _pool(self, prefix: str, groups: list[GearGroup], threshold: float) -> list[GearGroup]:
        scored = [
            (self.answers.nouls[f"{prefix}:{group.key}"].noul, group)
            for group in groups
            if f"{prefix}:{group.key}" in self.answers.nouls
        ]
        scored = [(p, g) for p, g in scored if p >= threshold]
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [group for _, group in scored]

    def _cyberware(self) -> list[str]:
        if self.profile.is_awakened:
            return []
        groups = self._pool("cyberware", self.catalog.cyberware, CYBERWARE_THRESHOLD)
        has_eyes = any(g.hint == "eyeware" for g in groups)
        picked, essence = [], 0.0
        for group in groups:
            if group.hint == "eyewaremod" and not has_eyes:
                continue
            gear_id = self._variant(group)
            cost = ALL_GEAR[gear_id].essence or 0.0
            if essence + cost > ESSENCE_BUDGET:
                continue
            picked.append(gear_id)
            essence += cost
            if len(picked) == MAX_CYBERWARE:
                break
        return picked

    def gear_ids(self) -> list[str]:
        result = [self.answers.choices["armor"].choice]
        result += [
            gear_id
            for gear_id in self.catalog.helmets_and_shields
            if self.answers.nouls[f"armor:{gear_id}"].noul >= NOUL_THRESHOLD
        ]
        for slot in WEAPON_SLOTS:
            result += self._weapon(slot)
        result.append(self._device())
        if self.answers.nouls["fake_sin"].noul >= NOUL_THRESHOLD:
            result += [self._rated(self.catalog.fake_sins), self._rated(self.catalog.fake_licenses)]
        result += self._cyberware()
        result += [self._variant(g) for g in self._pool("gear", self.catalog.field_gear, GEAR_THRESHOLD)[:MAX_FIELD_GEAR]]
        if self.profile.is_decker:
            result += [self._variant(g) for g in self._pool("software", self.catalog.software, GEAR_THRESHOLD)[:MAX_SOFTWARE]]
        return result


def npc_state(values: dict) -> dict:
    return {"npc": {k: v for k, v in values.items() if k != "equipment"}}


class JevEquipmentFill:
    def __init__(self, entity, schema: str = "sr6equipment"):
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
        values = self.entity.values
        catalog = EquipmentCatalog.build()
        profile = NpcProfile.from_values(values)
        state = npc_state(values)
        questions = build_questions(catalog, profile)

        request = GptRequest(kind=self.__class__.__name__)
        request.input = {"state": state, "questions": list(questions)}
        try:
            answers = TypeSafeClient(model=config.JEV_MODEL).system_one(state, questions)
        except TypeSafeError as e:
            logging.info(f"Jev Error: {e}")
            request.output = str(e)
            request.failed()
            request.save()
            return Failure("jev_raised_an_error", e)

        equipment = [{"id": gear_id} for gear_id in Selection(catalog, profile, answers).gear_ids()]
        request.output = json.dumps(
            {"request_id": answers.request_id, "usage": answers.usage.model_dump() if answers.usage else None, "equipment": equipment}
        )
        request.finished()
        request.save()

        self.entity.add_values({"equipment": equipment})
        self.entity.save()
        return Success({"equipment": equipment})
