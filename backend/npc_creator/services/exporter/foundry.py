import math

from .foundry_template import (
    RootNPC,
    DefenseRating,
    ModWrapper,
    Gear,
    Item,
    FlagsUNDOCUMENTED,
    ExportSource,
)
import re
import sys, os
from PIL import Image, ImageDraw
import io
import base64
from npc_creator.services.exporter.foundry_template import (
    ActorNPC,
    ActorPlayer,
    Attributes,
    Stat,
    MagicAttr,
    ResAttr,
    EdgAttr,
    EssenceAttr,
    Skills,
    Skill,
)
from ...game_mechanics.armor import Armor
from ...game_mechanics.weapons import Weapon


def base64_encoded_image(content: bytes) -> bytes:
    img = base64.b64encode(content)
    return b"data:image/png;base64," + img


def translate_metatype(metatype: str) -> str:
    return metatype


def translate_magictype(npc) -> str:
    return "Unknown"


def cut_potrait(image_path, center=None, radius=None):
    # Open the input image
    image = Image.open(image_path).convert("RGBA")

    # Determine the size of the image
    width, height = image.size
    # If no radius is specified, calculate it based on the image size
    if radius is None:
        radius = min(width, height) // 2

    # If no center is specified, use the center of the image
    if center is None:
        center = (width // 2, radius)

    # Create a black mask with the same size as the image
    mask = Image.new("L", (width, height), 0)

    # Draw a white circle on the mask
    draw = ImageDraw.Draw(mask)
    left_up_point = (center[0] - radius, center[1] - radius)
    right_down_point = (center[0] + radius, center[1] + radius)
    draw.ellipse([left_up_point, right_down_point], fill=255)

    # Apply the mask to the image
    result = Image.new("RGBA", (radius * 2, radius * 2))
    result.paste(image, (-center[0] + radius, -center[1] + radius), mask=mask)

    # Save the resulting image to a bytes buffer
    buffered = io.BytesIO()
    result.save(buffered, format="png")
    return buffered.getvalue()


def foundry_armor(armor: Armor) -> Gear:
    return Item(
        type="gear",
        name=armor.name,
        system=Gear(
            type=armor.type,
            subtype=armor.subtype,
            count=1,
            countable=True,
            availDef=str(armor.availability),
            avail=armor.availability,
            priceDef=str(armor.cost or ""),
            price=armor.cost,
            customName=armor.name,
            defense=armor.defense_rating,
            capacity=armor.capacity,
            usedForPool=True,
        ),
    )


def foundry_weapon(weapon: Weapon) -> Gear:
    return Item(
        type="gear",
        name=weapon.name,
        system=Gear(
            type=weapon.kind,
            subtype=weapon.subtype,
            count=1,
            countable=True,
            availDef=weapon.avail,
            avail=weapon.avail,
            priceDef=str(weapon.price or ""),
            price=weapon.price,
            customName=weapon.name,
            ammocap=weapon.cnt or 0,
            ammocount=weapon.cnt or 0,
            skill=weapon.skill,
            skillSpec=weapon.subtype.lower(),
            dmg=weapon.damage,
            stun=weapon.damage_type == "S",
            dmgDef=f"{weapon.damage}{weapon.damage_type or ''} {weapon.damage_note}",
            attackRating=[r or 0 for r in weapon.attack_rating],
            modes={"BF": weapon.bf, "FA": weapon.fa, "SA": weapon.sa, "SS": weapon.ss},
        ),
    )


def unarmed_weapon(npc) -> Gear:
    dmg = math.ceil(int(npc.values["strength"]) / 2)
    attack_rating = int(npc.values["strength"]) + int(npc.values["reaction"])
    return Item(
        type="gear",
        name="Unarmed",
        system=Gear(
            type="WEAPON_CLOSE_COMBAT",
            subtype="unarmed",
            count=1,
            countable=False,
            availDef="0",
            avail=0,
            priceDef="0",
            price=0,
            customName="Unarmed",
            dmg=dmg,
            stun=True,
            dmgDef=f"{dmg}S Stun",
            attackRating=[attack_rating, 0, 0, 0, 0],
            skill="close_combat",
            skillSpec="close combat",
        ),
    )


def foundry_json(npc):

    actor = ActorNPC(
        type=translate_magictype(npc),
        mortype=translate_magictype(npc),
        metatype=translate_metatype(npc.values["metatype"]),
        edge=EdgAttr(current=npc.values["edge"], max=npc.values["edge"]).model_dump(),
        attributes=Attributes(
            bod=Stat(base=npc.values["constitution"], pool=npc.values["constitution"]),
            agi=Stat(base=npc.values["agility"], pool=npc.values["agility"]),
            rea=Stat(base=npc.values["reaction"], pool=npc.values["reaction"]),
            str=Stat(base=npc.values["strength"], pool=npc.values["strength"]),
            wil=Stat(base=npc.values["willpower"], pool=npc.values["willpower"]),
            log=Stat(base=npc.values["logic"], pool=npc.values["logic"]),
            int=Stat(base=npc.values["intuition"], pool=npc.values["intuition"]),
            cha=Stat(base=npc.values["charisma"], pool=npc.values["charisma"]),
            mag=MagicAttr(base=npc.values["magic"], pool=npc.values["magic"]),
            res=ResAttr(base=npc.values["resonance"], pool=npc.values["resonance"]),
            edg=EdgAttr(current=npc.values["edge"], max=npc.values["edge"]),
            essence=EssenceAttr(base="6", pool="6"),
        ),
        skills=Skills(
            astral=Skill(base=npc.values["skill_astral"]),
            athletics=Skill(points=npc.values["skill_athletics"]),
            biotech=Skill(points=npc.values["skill_biotech"]),
            close_combat=Skill(points=npc.values["skill_close_combat"]),
            con=Skill(points=npc.values["skill_con"]),
            conjuring=Skill(points=npc.values["skill_conjuring"]),
            cracking=Skill(points=npc.values["skill_cracking"]),
            electronics=Skill(points=npc.values["skill_electronics"]),
            enchanting=Skill(points=npc.values["skill_enchanting"]),
            engineering=Skill(points=npc.values["skill_engineering"]),
            exotic_weapons=Skill(points=npc.values["skill_exotic_weapons"]),
            firearms=Skill(points=npc.values["skill_firearms"]),
            influence=Skill(points=npc.values["skill_influence"]),
            outdoors=Skill(points=npc.values["skill_outdoors"]),
            perception=Skill(points=npc.values["skill_perception"]),
            piloting=Skill(points=npc.values["skill_piloting"]),
            sorcery=Skill(points=npc.values["skill_sorcery"]),
            stealth=Skill(points=npc.values["skill_stealth"]),
            tasking=Skill(points=npc.values["skill_tasking"]),
        ),
        defenserating=DefenseRating(
            physical=ModWrapper(),
            matrix=ModWrapper(),
            astral=ModWrapper(),
        ),
    )

    if npc.image_set.exists():
        image = max(npc.image_set.all(), key=lambda x: x.score)
        try:
            img = base64_encoded_image(
                cut_potrait(
                    image.url,
                    radius=None,
                )
            )
        except FileNotFoundError:
            img = b""
    else:
        img = b""

    weapons = [foundry_weapon(weapon) for weapon in npc.weapons]
    armors = [foundry_armor(armor) for armor in npc.armors]

    root_npc = RootNPC(
        name=npc.values["name"],
        img=img,
        data=actor.model_dump(),
        items=weapons
        + armors
        + [
            unarmed_weapon(npc),
        ],
        flags=FlagsUNDOCUMENTED(export_source=ExportSource(npc_uuid=str(npc.uuid))),
    )

    return root_npc.model_dump_json(indent=2)
