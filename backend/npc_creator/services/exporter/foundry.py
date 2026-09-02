"""Export an NPC as Foundry VTT ``shadowrun6-eden`` actor JSON.

The output is what the eden system's native *Import Data* action consumes for an
Actor of type ``npc``. See :mod:`.foundry_template` for the target schema.

The exporter is strict: :func:`assert_exportable` raises :class:`ExportError`
unless the NPC carries clean SR6 mechanical data (all attributes, all 19 skills,
a valid metatype, and an ``equipment`` list whose every entry resolves to known
gear). Callers turn that into an HTTP 422 so the user learns why the download
was refused. NPCs are run through the SR6 fill pipeline before export, so a
failure here means the fill produced something unusable.
"""

import base64
import io
import logging

from PIL import Image, ImageDraw

from npc_creator.game_mechanics.manager import ALL_GEAR
from npc_creator.game_mechanics.reference_names import name_for
from npc_creator.game_mechanics.sr6.character import Metatype
from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.services.exporter.foundry_template import (
    SKILL_NAMES,
    ActorNPC,
    Attributes,
    EdgAttr,
    EdgeStat,
    EssenceAttr,
    ExportSource,
    Flags,
    FoundryGear,
    Item,
    MagicAttr,
    ResAttr,
    RootNPC,
    Skill,
    Skills,
    Stat,
    Tradition,
    parse_int,
)

log = logging.getLogger(__name__)


class ExportError(RuntimeError):
    """An NPC lacks the clean SR6 data a Foundry export needs."""


# eden attribute key -> npc.values key
ATTR_SOURCE = {
    "bod": "constitution",
    "agi": "agility",
    "rea": "reaction",
    "str": "strength",
    "wil": "willpower",
    "log": "logic",
    "int": "intuition",
    "cha": "charisma",
}

VALID_METATYPES = {m.value for m in Metatype}

# ObjectType -> eden Item("gear").system.type for non-weapon, non-armor gear
GENERIC_GEAR_TYPE = {
    ObjectType.Armor: "ARMOR",
    ObjectType.Cyberware: "CYBERWARE",
    ObjectType.CyberwareMod: "CYBERWARE",
    ObjectType.Biotech: "BIOWARE",
    ObjectType.Commlink: "ELECTRONICS",
    ObjectType.Cyberdeck: "ELECTRONICS",
    ObjectType.CommunicationGear: "ELECTRONICS",
    ObjectType.OpticalDevice: "ELECTRONICS",
    ObjectType.OpticalDeviceMod: "ELECTRONICS",
    ObjectType.AudioDevice: "ELECTRONICS",
    ObjectType.AudioDeviceMod: "ELECTRONICS",
    ObjectType.Sensorhousing: "ELECTRONICS",
    ObjectType.SensorhousingMod: "ELECTRONICS",
    ObjectType.RFID: "ELECTRONICS",
    ObjectType.Software: "SOFTWARE",
    ObjectType.Tool: "TOOLS",
    ObjectType.Security: "TOOLS",
    ObjectType.BreakingEntering: "TOOLS",
    ObjectType.SurvivalGear: "TOOLS",
    ObjectType.Grapple: "TOOLS",
    ObjectType.Chemical: "ACCESSORY",
    ObjectType.Accessory: "ACCESSORY",
    ObjectType.WeaponMod: "ACCESSORY",
    ObjectType.Credstick: "ACCESSORY",
    ObjectType.License: "ACCESSORY",
    ObjectType.SIN: "ACCESSORY",
}


# --------------------------------------------------------------------------- #
# small helpers
# --------------------------------------------------------------------------- #
def _clean_int(value):
    """Return ``value`` as an int, or ``None`` if it is not a plain number.

    Accepts ints and numeric strings (``"3"``); rejects ``None``, booleans,
    dicts, lists and free text.
    """
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


def _avail_number(avail) -> int:
    """Leading integer of an availability string (``"8F"`` -> 8)."""
    digits = ""
    for char in str(avail or ""):
        if char.isdigit():
            digits += char
        else:
            break
    return int(digits) if digits else 0


def _equipment_id(entry):
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict):
        return entry.get("id")
    return None


def _display_name(gear: Gear) -> str:
    return name_for(gear.id)


# --------------------------------------------------------------------------- #
# strict precondition
# --------------------------------------------------------------------------- #
def assert_exportable(npc) -> None:
    values = npc.values or {}
    problems: list[str] = []

    for key in (*ATTR_SOURCE.values(), "edge", "magic", "resonance"):
        if _clean_int(values.get(key)) is None:
            problems.append(key)

    for name in SKILL_NAMES:
        if _clean_int(values.get(f"skill_{name}")) is None:
            problems.append(f"skill_{name}")

    if values.get("metatype_enum") not in VALID_METATYPES:
        problems.append("metatype_enum")

    equipment = values.get("equipment")
    if not isinstance(equipment, list):
        problems.append("equipment (not a list)")
    else:
        for entry in equipment:
            gear_id = _equipment_id(entry)
            if not gear_id or gear_id not in ALL_GEAR:
                problems.append(f"equipment entry {entry!r}")

    if problems:
        raise ExportError(
            "This NPC is missing clean SR6 data and cannot be exported to "
            "Foundry. Re-run the SR6 fill and try again. Unusable: "
            + ", ".join(problems)
        )


# --------------------------------------------------------------------------- #
# portrait
# --------------------------------------------------------------------------- #
def _circle_crop(raw: bytes) -> bytes:
    image = Image.open(io.BytesIO(raw)).convert("RGBA")
    width, height = image.size
    radius = min(width, height) // 2
    center = (width // 2, radius)

    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(
        [center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius],
        fill=255,
    )

    result = Image.new("RGBA", (radius * 2, radius * 2))
    result.paste(image, (-center[0] + radius, -center[1] + radius), mask=mask)

    buffer = io.BytesIO()
    result.save(buffer, format="png")
    return buffer.getvalue()


def _portrait_data_uri(npc) -> str | None:
    images = [img for img in npc.image_set.all() if img.file]
    if not images:
        return None
    image = max(images, key=lambda img: img.score)
    try:
        with image.file.open("rb") as handle:
            raw = handle.read()
        encoded = base64.b64encode(_circle_crop(raw)).decode("ascii")
        return "data:image/png;base64," + encoded
    except Exception:  # storage miss, unreadable file, decode error
        log.warning(
            "foundry export: portrait unavailable for npc %s", npc.uuid, exc_info=True
        )
        return None


# --------------------------------------------------------------------------- #
# gear -> items
# --------------------------------------------------------------------------- #
def _weapon_eden_type(gear: Gear) -> str:
    skill = (gear.skill or "").lower()
    if skill == "close_combat":
        return "WEAPON_CLOSE_COMBAT"
    if skill == "exotic_weapons":
        return "WEAPON_SPECIAL"
    if skill in ("athletics", "archery"):
        return "WEAPON_RANGED"
    return "WEAPON_FIREARMS"


def _common_gear_fields(gear: Gear) -> dict:
    name = _display_name(gear)
    return dict(
        genesisID=gear.id,
        description=gear.rule or "",
        subtype=(gear.subtype or "").upper(),
        availDef=str(gear.avail or ""),
        avail=_avail_number(gear.avail),
        priceDef=str(gear.cost or ""),
        price=gear.cost or 0,
        customName=name,
        rating=gear.rating or 0,
    )


def _weapon_item(gear: Gear) -> Item:
    damage = gear.damage.mod
    damage_type = gear.damage_type.value or "P"
    note = f" {gear.damage_note}" if gear.damage_note else ""
    return Item(
        name=_display_name(gear),
        system=FoundryGear(
            **_common_gear_fields(gear),
            type=_weapon_eden_type(gear),
            skill=gear.skill or "",
            skillSpec=(gear.subtype or "").lower(),
            dmg=damage,
            stun=damage_type == "S",
            dmgDef=f"{damage}{damage_type}{note}".strip(),
            attackRating=[
                gear.attack_rating_0.mod,
                gear.attack_rating_1.mod,
                gear.attack_rating_2.mod,
                gear.attack_rating_3.mod,
                gear.attack_rating_4.mod,
            ],
            modes={
                "SS": bool(gear.ss),
                "SA": bool(gear.sa),
                "BF": bool(gear.bf),
                "FA": bool(gear.fa),
            },
            ammocap=parse_int(gear.cnt, 0),
            ammocount=parse_int(gear.cnt, 0),
            usedForPool=True,
        ),
    )


def _armor_item(gear: Gear) -> Item:
    return Item(
        name=_display_name(gear),
        system=FoundryGear(
            **_common_gear_fields(gear),
            type="ARMOR",
            defense=gear.defense_rating or 0,
            social=gear.social_rating or 0,
            capacity=gear.capacity or 0,
            usedForPool=True,
        ),
    )


def _generic_item(gear: Gear) -> Item:
    return Item(
        name=_display_name(gear),
        system=FoundryGear(
            **_common_gear_fields(gear),
            type=GENERIC_GEAR_TYPE.get(gear.type, "ACCESSORY"),
            essence=gear.essence or 0,
            devRating=gear.device_rating or 0,
        ),
    )


def _gear_item(gear: Gear) -> Item:
    if gear.type == ObjectType.Weapon:
        return _weapon_item(gear)
    if gear.type == ObjectType.Armor:
        return _armor_item(gear)
    return _generic_item(gear)


def _unarmed_item(npc) -> Item:
    # SR6 GRW p. 112: unarmed melee base damage is a flat 2S; Strength feeds the
    # dice pool, not the damage value.
    attack_rating = _clean_int(npc.values["strength"]) + _clean_int(
        npc.values["reaction"]
    )
    return Item(
        name="Unbewaffnet",
        system=FoundryGear(
            type="WEAPON_CLOSE_COMBAT",
            subtype="UNARMED",
            customName="Unbewaffnet",
            count=1,
            countable=False,
            dmg=2,
            stun=True,
            dmgDef="2S",
            attackRating=[attack_rating, 0, 0, 0, 0],
            skill="close_combat",
            skillSpec="unarmed",
            usedForPool=True,
        ),
    )


# --------------------------------------------------------------------------- #
# entrypoint
# --------------------------------------------------------------------------- #
def _mortype(magic: int, resonance: int) -> str:
    if resonance > 0:
        return "technomancer"
    if magic > 0:
        return "magician"
    return "mundane"


def foundry_json(npc) -> str:
    assert_exportable(npc)
    values = npc.values

    magic = _clean_int(values["magic"])
    resonance = _clean_int(values["resonance"])
    edge = _clean_int(values["edge"])
    mortype = _mortype(magic, resonance)

    gears = [ALL_GEAR[_equipment_id(entry)] for entry in values["equipment"]]

    essence = 6.0
    for gear in gears:
        if gear.essence:
            essence -= gear.essence
    essence = max(essence, 0.0)

    attributes = Attributes(
        **{
            eden_key: Stat(
                base=_clean_int(values[source]), pool=_clean_int(values[source])
            )
            for eden_key, source in ATTR_SOURCE.items()
        },
        mag=MagicAttr(base=magic, pool=magic),
        res=ResAttr(base=resonance, pool=resonance),
        edg=EdgAttr(current=edge, max=edge),
        essence=EssenceAttr(base=essence, pool=essence),
    )

    skills = Skills(
        **{
            name: Skill(points=_clean_int(values[f"skill_{name}"]))
            for name in SKILL_NAMES
        }
    )

    actor = ActorNPC(
        attributes=attributes,
        metatype=values["metatype_enum"],
        type="npc",
        mortype=mortype,
        gender=values.get("gender_enum") or "",
        skills=skills,
        edge=EdgeStat(value=edge, max=edge),
        tradition=Tradition(attribute="wil" if mortype == "technomancer" else "log"),
    )

    items = [_gear_item(gear) for gear in gears] + [_unarmed_item(npc)]

    root = RootNPC(
        name=values.get("name") or "NPC",
        img=_portrait_data_uri(npc),
        system=actor,
        items=items,
        flags=Flags(exportSource=ExportSource(npc_uuid=str(npc.uuid))),
    )

    return root.model_dump_json(indent=2, exclude_none=True)
