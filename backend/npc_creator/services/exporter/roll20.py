"""Export an NPC as Genesis / Roll20 Shadowrun 6E character JSON.

The output is the ``"system": "SHADOWRUN6"`` format the Roll20 SR6 character
sheet imports (see :mod:`.roll20_templates`). Unlike the Foundry export, the
Roll20 schema carries fully computed numbers (derived pools, condition
monitors, initiatives, weapon dice pools), so this exporter builds an
:class:`SR6Character`, runs the SR6 core rules over it and reads the results
back out.

The strict precondition gate is shared with the Foundry exporter
(:func:`npc_creator.services.exporter.foundry.assert_exportable`): a failure
raises :class:`ExportError`, which the view turns into an HTTP 422.
"""

import logging
import re

from npc_creator.game_mechanics.manager import ALL_GEAR
from npc_creator.game_mechanics.reference_names import name_for
from npc_creator.game_mechanics.sr6.character import (
    Astral,
    Athletics,
    Attributes,
    Biotech,
    CloseCombat,
    Con,
    Conjuring,
    Cracking,
    Electronics,
    Enchanting,
    Engineering,
    ExoticWeapons,
    Firearms,
    Influence,
    Outdoors,
    Perception,
    Piloting,
    SR6Character,
    Skills,
    Sorcery,
    Stealth,
    Tasking,
)
from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.sr6.gear_collection import GearCollection
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.services.exporter.foundry import (
    ExportError,
    _avail_number,
    _clean_int,
    _equipment_id,
    assert_exportable,
)
from npc_creator.services.exporter.roll20_templates import (
    R20Armor,
    R20Attribute,
    R20Augmentation,
    R20Character,
    R20CloseCombatWeapon,
    R20Initiative,
    R20Item,
    R20License,
    R20LongRangeWeapon,
    R20MatrixItem,
    R20Sin,
    R20Skill,
)

log = logging.getLogger(__name__)

UNARMED_ID = "sr6core/weapon/unarmed"

# npc.values skill suffix -> (SR6 skill class, german label, governing attribute)
SKILLS = {
    "astral": (Astral, "Astral", "intuition"),
    "athletics": (Athletics, "Athletik", "agility"),
    "biotech": (Biotech, "Biotech", "logic"),
    "close_combat": (CloseCombat, "Nahkampf", "agility"),
    "con": (Con, "Schwindeln", "charisma"),
    "conjuring": (Conjuring, "Beschwören", "magic"),
    "cracking": (Cracking, "Cracken", "logic"),
    "electronics": (Electronics, "Elektronik", "logic"),
    "enchanting": (Enchanting, "Verzaubern", "magic"),
    "engineering": (Engineering, "Mechanik", "logic"),
    "exotic_weapons": (ExoticWeapons, "Exotische Waffen", "agility"),
    "firearms": (Firearms, "Feuerwaffen", "agility"),
    "influence": (Influence, "Beeinflussung", "charisma"),
    "outdoors": (Outdoors, "Naturkunde", "intuition"),
    "perception": (Perception, "Wahrnehmung", "intuition"),
    "piloting": (Piloting, "Steuern", "reaction"),
    "sorcery": (Sorcery, "Zauberei", "magic"),
    "stealth": (Stealth, "Heimlichkeit", "agility"),
    "tasking": (Tasking, "Tasking", "resonance"),
}

# npc.values attribute key -> (roll20 id, german label)
ATTRIBUTES = {
    "constitution": ("BODY", "Konstitution"),
    "agility": ("AGILITY", "Geschicklichkeit"),
    "reaction": ("REACTION", "Reaktion"),
    "strength": ("STRENGTH", "Stärke"),
    "willpower": ("WILLPOWER", "Willenskraft"),
    "logic": ("LOGIC", "Logik"),
    "intuition": ("INTUITION", "Intuition"),
    "charisma": ("CHARISMA", "Charisma"),
    "edge": ("EDGE", "Edge"),
    "magic": ("MAGIC", "Magie"),
    "resonance": ("RESONANCE", "Resonanz"),
}
ATTR_GERMAN = {
    "body": "Konstitution",
    "agility": "Geschicklichkeit",
    "reaction": "Reaktion",
    "strength": "Stärke",
    "willpower": "Willenskraft",
    "logic": "Logik",
    "intuition": "Intuition",
    "charisma": "Charisma",
    "magic": "Magie",
    "resonance": "Resonanz",
}

GENDER = {"male": "MALE", "female": "FEMALE", "divers": "DIVERSE", "other": "OTHER"}

# firing modes -> Genesis german fire-mode codes (comma-separated, e.g. "HM,SM,AM")
FIRE_MODES = (("ss", "EM"), ("sa", "HM"), ("bf", "SM"), ("fa", "AM"))

DAMAGE_TYPE = {"P": "K", "S": "B"}

WEAPON_TYPE = {
    "firearms": "Feuerwaffen",
    "close_combat": "Nahkampfwaffen",
    "exotic_weapons": "Exotische Waffen",
    "athletics": "Projektilwaffen",
}
# weapon subtype id -> german label (best-effort; Genesis itself is inconsistent here)
WEAPON_SUBTYPE = {
    "holdouts": "Holdouts",
    "pistols_light": "Leichte Pistolen",
    "pistols_heavy": "Schwere Pistolen",
    "machine_pistols": "Maschinenpistolen",
    "submachine_guns": "Maschinenpistolen",
    "assault_rifle": "Sturmgewehre",
    "shotguns": "Schrotflinten",
    "mmg": "Mittleres MG",
    "hmg": "Schweres MG",
    "assault_cannon": "Sturmkanonen",
    "tasers": "Taser",
    "crossbows": "Armbrüste",
    "throwing": "Wurfwaffen",
    "whips": "Peitschen",
    "unarmed": "Handgemenge",
    "blades": "Klingen",
    "clubs": "Knüppel",
    "close_combat": "Nahkampf",
    "special": "Spezialwaffen",
}
MATRIX_SUBTYPE = {ObjectType.Commlink: "COMMLINK", ObjectType.Cyberdeck: "CYBERDECK"}
AUGMENTATION_TYPES = (ObjectType.Cyberware, ObjectType.CyberwareMod, ObjectType.Biotech)
MATRIX_TYPES = (ObjectType.Commlink, ObjectType.Cyberdeck)
# gear that gets its own dedicated section instead of the generic ``items`` list
DEDICATED_TYPES = {
    ObjectType.Weapon,
    ObjectType.Armor,
    ObjectType.SIN,
    ObjectType.License,
    *AUGMENTATION_TYPES,
    *MATRIX_TYPES,
}


# --------------------------------------------------------------------------- #
# NPC -> SR6Character
# --------------------------------------------------------------------------- #
def _character_from_npc(npc) -> SR6Character:
    """Build an :class:`SR6Character` from a (gate-checked) NPC and run rules."""
    values = npc.values

    attributes = Attributes(
        body=_clean_int(values["constitution"]),
        agility=_clean_int(values["agility"]),
        reaction=_clean_int(values["reaction"]),
        strength=_clean_int(values["strength"]),
        willpower=_clean_int(values["willpower"]),
        logic=_clean_int(values["logic"]),
        intuition=_clean_int(values["intuition"]),
        charisma=_clean_int(values["charisma"]),
        edge=_clean_int(values["edge"]),
        magic=_clean_int(values["magic"]),
        resonance=_clean_int(values["resonance"]),
    )
    skills = Skills(
        **{
            name: cls(points=_clean_int(values[f"skill_{name}"]))
            for name, (cls, _label, _attr) in SKILLS.items()
        }
    )

    unarmed = ALL_GEAR[UNARMED_ID].model_copy(deep=True)
    char = SR6Character(
        uuid=str(npc.uuid),
        name=values.get("name") or "",
        street_name=_street_name(values),
        size="",
        weight="",
        age=str(values.get("age") or ""),
        gender=values.get("gender_enum") or "other",
        metatype=values["metatype_enum"],
        attributes=attributes,
        skills=skills,
        gear=GearCollection(),
        unarmed=unarmed,
    )
    char.enable_base_rules()

    for entry in values["equipment"]:
        gear = ALL_GEAR.get(_equipment_id(entry))
        if gear is not None:
            char.add_gear(gear.model_copy(deep=True))
    char.add_gear(unarmed)

    return char


_HANDLE_RE = re.compile(r'["“„](.*?)["”“]')


def _street_name(values) -> str:
    """The handle in quotes inside the generated name, e.g. Jane "Spark" Doe."""
    match = _HANDLE_RE.search(values.get("name") or "")
    return match.group(1) if match else ""


def _legal_name(values):
    """The name with the quoted handle removed (Genesis keeps the two apart)."""
    name = values.get("name")
    if not name:
        return None
    return _HANDLE_RE.sub("", name).replace("  ", " ").strip() or None


# --------------------------------------------------------------------------- #
# section builders
# --------------------------------------------------------------------------- #
def _attributes(char: SR6Character) -> list[R20Attribute]:
    rows = [
        R20Attribute(
            name=label,
            id=r20_id,
            points=getattr(char.attributes, _ATTR_FIELD[key]).points,
            modifiedValue=getattr(char.attributes, _ATTR_FIELD[key]).mod,
        )
        for key, (r20_id, label) in ATTRIBUTES.items()
    ]
    rows.append(R20Attribute(name="Kraftpunkte", id="POWER_POINTS", points=0, modifiedValue=0))
    for field, r20_id, label in (
        ("defense_pool_physical", "DEFENSE_POOL_PHYSICAL", "Verteidigungspool"),
        ("composure", "COMPOSURE", "Selbstbeherrschung"),
        ("judge_intentions", "JUDGE_INTENTIONS", "Menschenkenntnis"),
        ("memory", "MEMORY", "Erinnerungsvermögen"),
        ("lift_carry", "LIFT_CARRY", "Heben / Tragen"),
    ):
        rows.append(
            R20Attribute(
                name=label, id=r20_id, points=0, modifiedValue=getattr(char, field).mod
            )
        )
    return rows


_ATTR_FIELD = {
    "constitution": "body",
    "agility": "agility",
    "reaction": "reaction",
    "strength": "strength",
    "willpower": "willpower",
    "logic": "logic",
    "intuition": "intuition",
    "charisma": "charisma",
    "edge": "edge",
    "magic": "magic",
    "resonance": "resonance",
}


def _initiatives(char: SR6Character) -> list[R20Initiative]:
    return [
        R20Initiative(
            name="Initiative (Astral)",
            id="INITIATIVE_ASTRAL",
            value=char.astral_initiative_base.mod,
            dice=f"+{char.astral_initiative_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative",
            id="INITIATIVE_PHYSICAL",
            value=char.physical_initiative_base.mod,
            dice=f"+{char.physical_initiative_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative (Matrix)",
            id="INITIATIVE_MATRIX",
            value=char.initiative_matrix_ar_base.mod,
            dice=f"+{char.initiative_matrix_ar_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative (Matrix VR)",
            id="INITIATIVE_MATRIX_VR_COLD",
            value=char.initiative_matrix_vr_cold_base.mod,
            dice=f"+{char.initiative_matrix_vr_cold_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative (Matrix Hot)",
            id="INITIATIVE_MATRIX_VR_HOT",
            value=char.initiative_matrix_vr_hot_base.mod,
            dice=f"+{char.initiative_matrix_vr_hot_dices.mod}D6",
        ),
    ]


def _skills(char: SR6Character) -> list[R20Skill]:
    rows = []
    for name, (_cls, label, attr) in SKILLS.items():
        skill = getattr(char.skills, name)
        rows.append(
            R20Skill(
                name=label,
                id=name,
                attribute=ATTR_GERMAN.get(attr, attr),
                rating=skill.points,
                pool=max(skill.mod - skill.points, 0),
                specializations=[],
                influencedBy=[],
                description="",
            )
        )
    return rows


def _attack_rating(gear: Gear) -> str:
    brackets = [
        gear.attack_rating_0.mod,
        gear.attack_rating_1.mod,
        gear.attack_rating_2.mod,
        gear.attack_rating_3.mod,
        gear.attack_rating_4.mod,
    ]
    return "/".join(str(value) if value else "-" for value in brackets)


def _damage(gear: Gear) -> str:
    raw = gear.damage_type.value or "P"
    return f"{gear.damage.mod}{DAMAGE_TYPE.get(raw, raw)}"


def _fire_mode(gear: Gear) -> str | None:
    codes = [code for field, code in FIRE_MODES if getattr(gear, field)]
    return ",".join(codes) if codes else None


def _weapon_pool(char: SR6Character, gear: Gear) -> int:
    skill_name = (gear.skill or "").lower()
    entry = SKILLS.get(skill_name)
    if entry is None:
        return 0
    _cls, _label, attr_key = entry
    skill = getattr(char.skills, skill_name, None)
    attribute = getattr(char.attributes, attr_key, None)
    pool = 0
    if skill is not None:
        pool += skill.mod
    if attribute is not None:
        pool += attribute.mod
    return pool


def _weapons(char: SR6Character):
    long_range: list[R20LongRangeWeapon] = []
    close_combat: list[R20CloseCombatWeapon] = []
    for gear in char.weapons:
        skill_name = (gear.skill or "").lower()
        subtype_id = (gear.subtype or "").lower()
        common = dict(
            name=name_for(gear.id),
            type=WEAPON_TYPE.get(skill_name, "Waffen"),
            subtype=WEAPON_SUBTYPE.get(subtype_id, (gear.subtype or "").replace("_", " ").title()),
            skill=None,
            pool=_weapon_pool(char, gear),
            damage=_damage(gear),
            attackRating=_attack_rating(gear),
            wifi=[],
            accessories=[],
            page="",
            description="",
            primary=False,
        )
        if skill_name == "close_combat":
            close_combat.append(R20CloseCombatWeapon(**common))
        else:
            long_range.append(
                R20LongRangeWeapon(
                    **common,
                    mode=_fire_mode(gear),
                    ammunition=str(gear.cnt or ""),
                )
            )
    return long_range, close_combat


def _armors(char: SR6Character) -> list[R20Armor]:
    rows = []
    for index, gear in enumerate(char.gear.filter(ObjectType.Armor)):
        rows.append(
            R20Armor(
                name=name_for(gear.id),
                rating=gear.defense_rating or 0,
                socialrating=0,
                accessories=[],
                isIgnored=False,
                page="",
                description="",
                primary=index == 0,
            )
        )
    return rows


def _augmentations(char: SR6Character) -> list[R20Augmentation]:
    rows = []
    for object_type in AUGMENTATION_TYPES:
        for gear in char.gear.filter(object_type):
            rows.append(
                R20Augmentation(
                    name=name_for(gear.id),
                    level=gear.rating,
                    essence=float(gear.essence or 0),
                    page="",
                    quality=None,
                    description="",
                    accessories=[],
                )
            )
    return rows


def _matrix_items(char: SR6Character) -> list[R20MatrixItem]:
    rows = []
    for object_type in MATRIX_TYPES:
        for gear in char.gear.filter(object_type):
            rows.append(
                R20MatrixItem(
                    name=name_for(gear.id),
                    dataProcessing=gear.D.mod,
                    firewall=gear.F.mod,
                    attack=gear.A.mod,
                    sleaze=gear.S.mod,
                    deviceRating=gear.device_rating or 0,
                    type="Elektronik und Technisches",
                    subType=MATRIX_SUBTYPE.get(object_type, ""),
                    page="",
                    concurrentPrograms=gear.active_program_slots.mod,
                    accessories=[],
                    programs=[],
                    description="",
                )
            )
    return rows


def _sins(char: SR6Character) -> list[R20Sin]:
    return [
        R20Sin(name=name_for(gear.id), description=None, quality=gear.rating or 0)
        for gear in char.gear.filter(ObjectType.SIN)
    ]


def _licenses(char: SR6Character) -> list[R20License]:
    return [
        R20License(name=name_for(gear.id), sin="", type=None, rating=str(gear.rating or ""))
        for gear in char.gear.filter(ObjectType.License)
    ]


def _items(char: SR6Character) -> list[R20Item]:
    rows = []
    for gear in char.gear:
        if gear.type in DEDICATED_TYPES:
            continue
        rows.append(
            R20Item(
                name=name_for(gear.id),
                count=1,
                rating=gear.rating or 0,
                type=str(gear.type).replace("_", " ").title(),
                subType=(gear.subtype or "").replace("_", " ").title(),
                page="",
                accessories=[],
                description="",
            )
        )
    return rows


# --------------------------------------------------------------------------- #
# entrypoint
# --------------------------------------------------------------------------- #
def roll20_character(npc) -> R20Character:
    assert_exportable(npc)
    values = npc.values
    char = _character_from_npc(npc)
    long_range, close_combat = _weapons(char)

    return R20Character(
        system="SHADOWRUN6",
        version="3.2.0",
        name=_legal_name(values),
        streetName=_street_name(values),
        metaType=values.get("metatype") or values["metatype_enum"],
        size=0,
        weight=0,
        age=None,
        gender=GENDER.get(values.get("gender_enum"), "OTHER"),
        heat=0,
        reputation=0,
        karma=0,
        freeKarma=0,
        nuyen=0,
        initiation=0,
        submersion=0,
        attributes=_attributes(char),
        initiatives=_initiatives(char),
        qualities=[],
        skills=_skills(char),
        spells=[],
        rituals=[],
        metamagic=None,
        echoes=None,
        complexForms=[],
        adeptPowers=[],
        longRangeWeapons=long_range,
        closeCombatWeapons=close_combat,
        armors=_armors(char),
        items=_items(char),
        augmentations=_augmentations(char),
        vehicles=[],
        drones=[],
        lifestyles=[],
        sins=_sins(char),
        contacts=[],
        licenses=_licenses(char),
        matrixItems=_matrix_items(char),
        martialArts=[],
        signatureManeuvers=[],
        notes=None,
    )


def roll20_json(npc) -> str:
    return roll20_character(npc).model_dump_json(indent=2)


__all__ = ["ExportError", "roll20_character", "roll20_json"]
