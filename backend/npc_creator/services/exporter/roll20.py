import copy
import logging
import uuid
from npc_creator.game_mechanics import startup
from npc_creator.game_mechanics.manager import ALL_GEAR, ALL_RULES
from npc_creator.game_mechanics.sr6.modifiable_value import ModifiableValue

from npc_creator.game_mechanics.sr6.character import (
    Astral,
    Athletics,
    Biotech,
    CloseCombat,
    Con,
    Conjuring,
    Cracking,
    Enchanting,
    Engineering,
    ExoticWeapons,
    Influence,
    Perception,
    Piloting,
    SR6Character,
    Attributes,
    Skills,
    Electronics,
    Firearms,
    Outdoors,
    Sorcery,
    Stealth,
    Tasking,
)
from npc_creator.game_mechanics.sr6.gear_collection import GearCollection
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.services.exporter.roll20_templates import (
    R20Character,
    R20Attribute,
    R20Initiative,
    R20Skill,
    R20Weapon,
    R20Item,
)


def translate_gender(gender: str):
    return {"männlich": "MALE", "weiblich": "FEMALE"}.get(gender.lower(), gender)


def roll20_npc(char: SR6Character) -> R20Character:
    attributes = [
        R20Attribute(
            name="Body",
            id="BODY",
            points=char.attributes.body.points,
            modifiedValue=char.attributes.body.mod,
        ),
        R20Attribute(
            name="Agility",
            id="AGILITY",
            points=char.attributes.agility.points,
            modifiedValue=char.attributes.agility.mod,
        ),
        R20Attribute(
            name="Reaction",
            id="REACTION",
            points=char.attributes.reaction.points,
            modifiedValue=char.attributes.reaction.mod,
        ),
        R20Attribute(
            name="Strength",
            id="STRENGTH",
            points=char.attributes.strength.points,
            modifiedValue=char.attributes.strength.mod,
        ),
        R20Attribute(
            name="Willpower",
            id="WILLPOWER",
            points=char.attributes.willpower.points,
            modifiedValue=char.attributes.willpower.mod,
        ),
        R20Attribute(
            name="Logic",
            id="LOGIC",
            points=char.attributes.logic.points,
            modifiedValue=char.attributes.logic.mod,
        ),
        R20Attribute(
            name="Intuition",
            id="INTUITION",
            points=char.attributes.intuition.points,
            modifiedValue=char.attributes.intuition.mod,
        ),
        R20Attribute(
            name="Charisma",
            id="CHARISMA",
            points=char.attributes.charisma.points,
            modifiedValue=char.attributes.charisma.mod,
        ),
        R20Attribute(
            name="Edge",
            id="EDGE",
            points=char.attributes.edge.points,
            modifiedValue=char.attributes.edge.mod,
        ),
        R20Attribute(
            name="Magic",
            id="MAGIC",
            points=char.attributes.magic.points,
            modifiedValue=char.attributes.magic.mod,
        ),
        R20Attribute(
            name="Resonance",
            id="RESONANCE",
            points=char.attributes.resonance.points,
            modifiedValue=char.attributes.resonance.mod,
        ),
        R20Attribute(
            name="Power points",
            id="POWER_POINTS",
            points=0,
            modifiedValue=0,
        ),
        R20Attribute(
            name="Defense pool (physical)",
            id="DEFENSE_POOL_PHYSICAL",
            points=char.defense_pool_physical.points,
            modifiedValue=char.defense_pool_physical.mod,
        ),
        R20Attribute(
            name="Composure",
            id="COMPOSURE",
            points=char.composure.points,
            modifiedValue=char.composure.mod,
        ),
        R20Attribute(
            name="Judge intentions",
            id="JUDGE_INTENTIONS",
            points=char.judge_intentions.points,
            modifiedValue=char.judge_intentions.mod,
        ),
        R20Attribute(
            name="Memory",
            id="MEMORY",
            points=char.memory.points,
            modifiedValue=char.memory.mod,
        ),
        R20Attribute(
            name="lift / carry",
            id="LIFT_CARRY",
            points=char.lift_carry.points,
            modifiedValue=char.lift_carry.mod,
        ),
    ]

    initiatives = [
        R20Initiative(
            name="Initiative (astral)",
            id="INITIATIVE_ASTRAL",
            value=char.astral_initiative_base.mod,
            dice=f"+{char.astral_initiative_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative (physical)",
            id="INITIATIVE_PHYSICAL",
            value=char.physical_initiative_base.mod,
            dice=f"+{char.physical_initiative_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative (matrix)",
            id="INITIATIVE_MATRIX",
            value=char.initiative_matrix_ar_base.mod,
            dice=f"+{char.initiative_matrix_ar_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative (matrix VR)",
            id="INITIATIVE_MATRIX_VR_COLD",
            value=char.initiative_matrix_vr_cold_base.mod,
            dice=f"+{char.initiative_matrix_vr_cold_dices.mod}D6",
        ),
        R20Initiative(
            name="Initiative (matrix Hot)",
            id="INITIATIVE_MATRIX_VR_HOT",
            value=char.initiative_matrix_vr_hot_base.mod,
            dice=f"+{char.initiative_matrix_vr_hot_dices.mod}D6",
        ),
    ]

    skills = [
        R20Skill(
            name="astral",
            id="astral",
            attribute="intuition",
            rating=char.skills.astral.points,
            pool=char.skills.astral.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="athletics",
            id="athletics",
            attribute="agility",
            rating=char.skills.athletics.points,
            pool=char.skills.athletics.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="biotech",
            id="biotech",
            attribute="logic",
            rating=char.skills.biotech.points,
            pool=char.skills.biotech.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="close_combat",
            id="close_combat",
            attribute="agility",
            rating=char.skills.close_combat.points,
            pool=char.skills.close_combat.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="con",
            id="con",
            attribute="charisma",
            rating=char.skills.con.points,
            pool=char.skills.con.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="conjuring",
            id="conjuring",
            attribute="magic",
            rating=char.skills.conjuring.points,
            pool=char.skills.conjuring.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="cracking",
            id="cracking",
            attribute="logic",
            rating=char.skills.cracking.points,
            pool=char.skills.cracking.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="electronics",
            id="electronics",
            attribute="logic",
            rating=char.skills.electronics.points,
            pool=char.skills.electronics.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="enchanting",
            id="enchanting",
            attribute="magic",
            rating=char.skills.enchanting.points,
            pool=char.skills.enchanting.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="engineering",
            id="engineering",
            attribute="logic",
            rating=char.skills.engineering.points,
            pool=char.skills.engineering.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="exotic_weapons",
            id="exotic_weapons",
            attribute="agility",
            rating=char.skills.exotic_weapons.points,
            pool=char.skills.exotic_weapons.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="firearms",
            id="firearms",
            attribute="agility",
            rating=char.skills.firearms.points,
            pool=char.skills.firearms.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="influence",
            id="influence",
            attribute="charisma",
            rating=char.skills.influence.points,
            pool=char.skills.influence.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="outdoors",
            id="outdoors",
            attribute="intuition",
            rating=char.skills.outdoors.points,
            pool=char.skills.outdoors.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="perception",
            id="perception",
            attribute="intuition",
            rating=char.skills.perception.points,
            pool=char.skills.perception.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="piloting",
            id="piloting",
            attribute="reaction",
            rating=char.skills.piloting.points,
            pool=char.skills.piloting.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="sorcery",
            id="sorcery",
            attribute="magic",
            rating=char.skills.sorcery.points,
            pool=char.skills.sorcery.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="stealth",
            id="stealth",
            attribute="agility",
            rating=char.skills.stealth.points,
            pool=char.skills.stealth.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="tasking",
            id="tasking",
            attribute="resonance",
            rating=char.skills.tasking.points,
            pool=char.skills.tasking.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="perception",
            id="perception",
            attribute="intuition",
            rating=char.skills.perception.points,
            pool=char.skills.perception.mod,
            specializations=[],
            influencedBy=[],
            description="",
        ),
        R20Skill(
            name="Muttersprache",
            id="language",
            attribute="logic",
            rating=6,
            pool=6,
            specializations=[],
            influencedBy=[],
            description="",
        ),
    ]

    qualities = []
    close_combat_weapons = [
        R20Weapon(
            name=w.name,
            type=w.kind,
            subtype=w.subtype,
            skill=w.skill,
            pool=w.cnt or 0,
            damage=w.damage,
            attackRating=str(
                [
                    w.attack_rating_0.mod,
                    w.attack_rating_1.mod,
                    w.attack_rating_2.mod,
                    w.attack_rating_3.mod,
                    w.attack_rating_4.mod,
                ]
            ),
            wifi=[],
            accessories=[],
            page="",
            description="",
            primary=getattr(w, "primary", False),
        )
        for w in getattr(npc, "weapons", [])
    ]
    items = [
        R20Item(
            name=i.name,
            count=i.count,
            rating=i.rating,
            type=i.type,
            subType=i.subType,
            page=i.page,
            accessories=i.accessories,
            description=i.description,
        )
        for i in getattr(npc, "items", [])
    ]
    drones = []
    matrixItems = []

    char = R20Character(
        system="SHADOWRUN6",
        version="3.2.0",
        name=char.name,
        streetName=char.street_name,
        metaType=char.metatype.name,
        size=0,  # char.size,
        weight=0,  # char.weight,
        age=0,  # get("age", 0),
        gender=char.gender.name,
        heat=0,
        reputation=0,
        karma=0,
        freeKarma=0,
        nuyen=0,
        initiation=0,
        submersion=0,
        attributes=attributes,
        initiatives=initiatives,
        qualities=qualities,
        skills=skills,
        spells=[],
        rituals=[],
        metamagic=None,
        echoes=None,
        complexForms=[],
        adeptPowers=[],
        longRangeWeapons=[],
        closeCombatWeapons=close_combat_weapons,
        armors=[],
        items=items,
        augmentations=[],
        vehicles=[],
        drones=drones,
        lifestyles=[],
        sins=[],
        contacts=[],
        licenses=[],
        matrixItems=matrixItems,
        martialArts=[],
        signatureManeuvers=[],
        notes=None,
    )

    return char


if __name__ == "__main__":
    import re

    def extract_streetname(name: str) -> str:
        match = re.search(r'"(.*?)"', name)
        return match.group(1) if match else ""

    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shadowrun.settings")

    import django

    django.setup()
    logging.basicConfig(level=logging.DEBUG)

    from npc_creator.models import Npc

    def char_from_npc(npc: Npc):
        print(npc.values.keys())
        unarmed_weapon = ALL_GEAR["sr6core/weapon/unarmed"]

        return SR6Character(
            uuid=str(npc.uuid),
            name=npc.values["name"],
            street_name=extract_streetname(npc.values["name"]),
            size="",
            weight="",
            age=str(npc.values["age"]),
            gender=npc.values["gender_enum"],
            metatype=npc.values["metatype_enum"],
            attributes=Attributes(
                body=ModifiableValue(points=npc.values["constitution"]),
                agility=ModifiableValue(points=npc.values["agility"]),
                reaction=ModifiableValue(points=npc.values["reaction"]),
                strength=ModifiableValue(points=npc.values["strength"]),
                willpower=ModifiableValue(points=npc.values["willpower"]),
                logic=ModifiableValue(points=npc.values["logic"]),
                intuition=ModifiableValue(points=npc.values["intuition"]),
                charisma=ModifiableValue(points=npc.values["charisma"]),
                edge=ModifiableValue(points=npc.values["edge"]),
                magic=ModifiableValue(points=npc.values["magic"]),
                resonance=ModifiableValue(points=npc.values["resonance"]),
            ),
            skills=Skills(
                astral=Astral(points=npc.values["skill_astral"]),
                athletics=Athletics(points=npc.values["skill_athletics"]),
                biotech=Biotech(points=npc.values["skill_biotech"]),
                close_combat=CloseCombat(points=npc.values["skill_close_combat"]),
                con=Con(points=npc.values["skill_con"]),
                conjuring=Conjuring(points=npc.values["skill_conjuring"]),
                cracking=Cracking(points=npc.values["skill_cracking"]),
                electronics=Electronics(points=npc.values["skill_electronics"]),
                engineering=Engineering(points=npc.values["skill_engineering"]),
                enchanting=Enchanting(points=npc.values["skill_enchanting"]),
                exotic_weapons=ExoticWeapons(points=npc.values["skill_exotic_weapons"]),
                firearms=Firearms(points=npc.values["skill_firearms"]),
                influence=Influence(points=npc.values["skill_influence"]),
                outdoors=Outdoors(points=npc.values["skill_outdoors"]),
                perception=Perception(points=npc.values["skill_perception"]),
                piloting=Piloting(points=npc.values["skill_piloting"]),
                sorcery=Sorcery(points=npc.values["skill_sorcery"]),
                stealth=Stealth(points=npc.values["skill_stealth"]),
                tasking=Tasking(points=npc.values["skill_tasking"]),
            ),
            gear=GearCollection(),
            unarmed=unarmed_weapon,
        )

    startup.startup()

    npc = Npc.objects.get(uuid="682cec70-f04b-4751-8ab2-390d19a27f09")
    char = char_from_npc(npc)
    char.enable_base_rules()

    print(
        f"Perception: {char.skills.perception.mod}, Visual: {char.skills.perception.visual.mod}"
    )

    for o in npc.weapons + npc.armors:
        char.add_gear(o)

    for id, gear in ALL_GEAR.items():
        if gear.is_mod:
            continue

        char.add_gear(gear)

        for mod in ALL_GEAR.mods_for(gear):
            gear.add_gear(mod)

    print(
        f"Perception: {char.skills.perception.mod}, Visual: {char.skills.perception.visual.mod}"
    )
    print(f"Unarmed {char.unarmed.damage_type.mod}")

    with open("roll20.json", mode="w") as file:
        file.write(roll20_npc(char).model_dump_json(indent=2))
