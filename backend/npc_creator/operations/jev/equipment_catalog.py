"""Groups the SR6 gear catalog into the slots and pools Jev chooses from.

Slots hold at most one item and are asked as a single ``Choice``; pools hold
any number of items and get one ``Noul`` per item group. Rating variants
(``medkit/1`` .. ``medkit/6``) and cyberlimb variants (side, synthetic/obvious)
collapse into one group, so Jev judges the item and code picks the variant.
"""

import re
from dataclasses import dataclass, field

from npc_creator.game_mechanics.manager import ALL_GEAR
from npc_creator.game_mechanics.reference_names import name_for
from npc_creator.game_mechanics.sr6.gear import Gear

_RATING_SUFFIX = re.compile(r"/(\d+)$")
_LIMB_SUFFIX = re.compile(r"/(synthetic|obvious)(/(left|right))?$")

RANGED_SUBTYPES = {
    "assault_rifle",
    "submachine_guns",
    "shotguns",
    "mmg",
    "hmg",
    "assault_cannon",
    "crossbows",
    "special",
}
SIDEARM_SUBTYPES = {
    "holdouts",
    "pistols_light",
    "pistols_heavy",
    "machine_pistols",
    "tasers",
}
MELEE_SUBTYPES = {"blades", "clubs", "unarmed", "close_combat", "whips", "throwing"}

FIELD_GEAR_TYPES = {
    "accessory",
    "audiodevice",
    "biotech",
    "breakingandentering",
    "chemical",
    "communicationgear",
    "grapple",
    "opticaldevice",
    "survivalgear",
    "tool",
    "rfid",
}
# security is mostly building fixtures; only restraints are carried gear
CARRIED_SECURITY = ("restraints", "manacles", "straps")
CYBERWARE_MOD_SUBTYPES = {"eyewaremod", "headwaremod"}
# implanted versions of the single commlink/cyberdeck device slot
DEVICE_IMPLANTS = ("/headware_commlink", "/headware_cyberdeck")


def _type(gear: Gear) -> str:
    return gear.id.split("/")[1]


def _subtype(gear: Gear) -> str:
    return str(gear.subtype or "").lower()


def _rating(gear_id: str) -> int | None:
    match = _RATING_SUFFIX.search(gear_id)
    return int(match.group(1)) if match else None


def group_key(gear_id: str) -> str:
    return _LIMB_SUFFIX.sub("", _RATING_SUFFIX.sub("", gear_id))


def _label(gear_id: str) -> str:
    name = name_for(gear_id)
    if _LIMB_SUFFIX.search(gear_id):
        # "Cyberarm (offensichtlich, rechts)": the variant is picked in code
        name = re.sub(r" \(.*\)$", "", name)
    return re.sub(r" \d+$", "", name)


@dataclass
class GearGroup:
    key: str
    label: str
    hint: str
    variants: list[str] = field(default_factory=list)

    @property
    def rated(self) -> bool:
        return all(_rating(v) is not None for v in self.variants)

    def describe(self) -> str:
        return f"{self.label} ({self.hint})"


def _hint(gear: Gear) -> str:
    return _subtype(gear) or _type(gear)


def _groups(gears: list[Gear]) -> list[GearGroup]:
    groups: dict[str, GearGroup] = {}
    for gear in gears:
        key = group_key(gear.id)
        if key not in groups:
            groups[key] = GearGroup(key, _label(gear.id), _hint(gear))
        groups[key].variants.append(gear.id)
    for group in groups.values():
        if group.rated:
            group.variants.sort(key=lambda v: _rating(v) or 0)
    return list(groups.values())


def _is_implant_weapon(gear: Gear) -> bool:
    return "/cyber_implant_weapon/" in gear.id


def _carried(gear: Gear) -> bool:
    if gear.is_mod:
        return False
    if _type(gear) == "security":
        return gear.id.endswith(CARRIED_SECURITY)
    if _type(gear) == "biotech":
        return "docwagon" not in gear.id
    return _type(gear) in FIELD_GEAR_TYPES


def _is_cyberware(gear: Gear) -> bool:
    if _type(gear) == "cyberware":
        return not gear.id.endswith(DEVICE_IMPLANTS)
    if _type(gear) == "cyberwaremod":
        return _subtype(gear) in CYBERWARE_MOD_SUBTYPES
    return _is_implant_weapon(gear)


@dataclass
class EquipmentCatalog:
    armor: list[str]
    helmets_and_shields: list[str]
    ranged: list[str]
    sidearms: list[str]
    melee: list[str]
    commlinks: list[str]
    cyberdecks: list[str]
    fake_sins: list[str]
    fake_licenses: list[str]
    cyberware: list[GearGroup]
    field_gear: list[GearGroup]
    software: list[GearGroup]

    @classmethod
    def build(cls) -> "EquipmentCatalog":
        gears = list(ALL_GEAR.values())

        def ids(predicate) -> list[str]:
            return [g.id for g in gears if predicate(g)]

        def weapon(subtypes):
            return lambda g: (
                _type(g) == "weapon"
                and _subtype(g) in subtypes
                and not _is_implant_weapon(g)
                and not g.id.endswith("/unarmed")
            )

        return cls(
            armor=ids(lambda g: _subtype(g) == "armor_body"),
            helmets_and_shields=ids(
                lambda g: _subtype(g) in ("armor_helmet", "armor_shield")
            ),
            ranged=ids(weapon(RANGED_SUBTYPES)),
            sidearms=ids(weapon(SIDEARM_SUBTYPES)),
            melee=ids(weapon(MELEE_SUBTYPES)),
            commlinks=sorted(ids(lambda g: _type(g) == "commlink"), key=_rating),
            cyberdecks=sorted(ids(lambda g: _type(g) == "cyberdeck"), key=_rating),
            fake_sins=sorted(ids(lambda g: _type(g) == "sin"), key=_rating),
            fake_licenses=sorted(ids(lambda g: _type(g) == "license"), key=_rating),
            cyberware=_groups([g for g in gears if _is_cyberware(g)]),
            field_gear=_groups([g for g in gears if _carried(g)]),
            software=_groups([g for g in gears if _type(g) == "software"]),
        )
