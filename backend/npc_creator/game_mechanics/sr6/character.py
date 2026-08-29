from enum import StrEnum
from typing import final

from pydantic import BaseModel, Field

from npc_creator.game_mechanics.manager import ALL_RULES
from npc_creator.game_mechanics.sr6.eval_errors import NotExistingAttributeError
from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.sr6.modifiable_object import ModifiableObject
from npc_creator.game_mechanics.sr6.modifiable_value import ModifiableValue
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.game_mechanics.sr6.rule import ModifierType
from npc_creator.game_mechanics.sr6.gear_collection import GearCollection
from npc_creator.game_mechanics.sr6.books import Rulebook


class Metatype(StrEnum):
    HUMAN = "human"
    ORK = "ork"
    DWARF = "dwarf"
    ELF = "elf"
    TROLL = "troll"
    SPIRIT = "spirit"
    AI = "ai"
    OGRE = "ogre"
    DRAKE = "drake"
    ONI = "oni"
    HOBGOBLIN = "hobgoblin"
    OTHER = "other"
    GIANT = "giant"
    CYCLOP = "cyclop"
    MINOTAUR = "minotaur"
    FOMORIAN = "fomorian"
    SATYR = "satyr"
    NOCTURNE = "nocturne"
    WAKYAMBI = "wakyambi"
    XAPIRI = "xapiri"
    DRYAD = "dryad"
    DALAKITNON = "dalakitnon"
    VALKYRIE = "valkyrie"
    NARTAKI = "nartaki"
    DUENDE = "duende"
    HANUMAN = "hanuman"
    MENEHUNE = "menehune"
    KOBOROKURU = "koborokuru"
    GNOME = "gnome"
    CENTAUR = "centaur"
    NAGA = "naga"
    PIXIE = "pixie"
    SASQUATCH = "sasquatch"


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"
    DIVERS = "divers"
    OTHER = "other"


class Attributes(BaseModel):
    body: ModifiableValue = Field(default_factory=ModifiableValue)
    agility: ModifiableValue = Field(default_factory=ModifiableValue)
    reaction: ModifiableValue = Field(default_factory=ModifiableValue)
    strength: ModifiableValue = Field(default_factory=ModifiableValue)
    willpower: ModifiableValue = Field(default_factory=ModifiableValue)
    logic: ModifiableValue = Field(default_factory=ModifiableValue)
    intuition: ModifiableValue = Field(default_factory=ModifiableValue)
    charisma: ModifiableValue = Field(default_factory=ModifiableValue)
    edge: ModifiableValue = Field(default_factory=ModifiableValue)
    magic: ModifiableValue = Field(default_factory=ModifiableValue)
    resonance: ModifiableValue = Field(default_factory=ModifiableValue)


class Astral(ModifiableValue):
    astral_combat: ModifiableValue = Field(default_factory=ModifiableValue)
    astral_signatures: ModifiableValue = Field(default_factory=ModifiableValue)
    emotional_states: ModifiableValue = Field(default_factory=ModifiableValue)
    spirit_types: ModifiableValue = Field(default_factory=ModifiableValue)


class Athletics(ModifiableValue):
    climbing: ModifiableValue = Field(default_factory=ModifiableValue)
    flying: ModifiableValue = Field(default_factory=ModifiableValue)
    gymnastics: ModifiableValue = Field(default_factory=ModifiableValue)
    sprinting: ModifiableValue = Field(default_factory=ModifiableValue)
    swimming: ModifiableValue = Field(default_factory=ModifiableValue)
    throwing: ModifiableValue = Field(default_factory=ModifiableValue)


class Biotech(ModifiableValue):
    biotechnology: ModifiableValue = Field(default_factory=ModifiableValue)
    cybertechnology: ModifiableValue = Field(default_factory=ModifiableValue)
    first_aid: ModifiableValue = Field(default_factory=ModifiableValue)
    medicine: ModifiableValue = Field(default_factory=ModifiableValue)


class CloseCombat(ModifiableValue):
    blades: ModifiableValue = Field(default_factory=ModifiableValue)
    clubs: ModifiableValue = Field(default_factory=ModifiableValue)
    unarmed_combat: ModifiableValue = Field(default_factory=ModifiableValue)


class Con(ModifiableValue):
    acting: ModifiableValue = Field(default_factory=ModifiableValue)
    disguise: ModifiableValue = Field(default_factory=ModifiableValue)
    impersonation: ModifiableValue = Field(default_factory=ModifiableValue)
    performance: ModifiableValue = Field(default_factory=ModifiableValue)


class Conjuring(ModifiableValue):
    banishing: ModifiableValue = Field(default_factory=ModifiableValue)
    binding: ModifiableValue = Field(default_factory=ModifiableValue)
    summoning: ModifiableValue = Field(default_factory=ModifiableValue)


class Cracking(ModifiableValue):
    cybercombat: ModifiableValue = Field(default_factory=ModifiableValue)
    electronic_warfare: ModifiableValue = Field(default_factory=ModifiableValue)
    hacking: ModifiableValue = Field(default_factory=ModifiableValue)


class Electronics(ModifiableValue):
    computer: ModifiableValue = Field(default_factory=ModifiableValue)
    hardware: ModifiableValue = Field(default_factory=ModifiableValue)
    software: ModifiableValue = Field(default_factory=ModifiableValue)
    complex_forms: ModifiableValue = Field(default_factory=ModifiableValue)


class Enchanting(ModifiableValue):
    alchemy: ModifiableValue = Field(default_factory=ModifiableValue)
    artificing: ModifiableValue = Field(default_factory=ModifiableValue)
    disenchanting: ModifiableValue = Field(default_factory=ModifiableValue)


class Engineering(ModifiableValue):
    aeronautics_mechanic: ModifiableValue = Field(default_factory=ModifiableValue)
    automotive_mechanic: ModifiableValue = Field(default_factory=ModifiableValue)
    demolitions: ModifiableValue = Field(default_factory=ModifiableValue)
    gunnery: ModifiableValue = Field(default_factory=ModifiableValue)
    industrial_mechanic: ModifiableValue = Field(default_factory=ModifiableValue)
    lockpicking: ModifiableValue = Field(default_factory=ModifiableValue)
    nautical_mechanic: ModifiableValue = Field(default_factory=ModifiableValue)


class ExoticWeapons(ModifiableValue):
    pass


class Firearms(ModifiableValue):
    # SR6 Grundregelwerk 3. Auflage / Errata S. 97: ten Feuerwaffen specializations
    holdout_pistols: ModifiableValue = Field(default_factory=ModifiableValue)
    light_pistols: ModifiableValue = Field(default_factory=ModifiableValue)
    heavy_pistols: ModifiableValue = Field(default_factory=ModifiableValue)
    machine_pistols: ModifiableValue = Field(default_factory=ModifiableValue)
    submachine_guns: ModifiableValue = Field(default_factory=ModifiableValue)
    rifles: ModifiableValue = Field(default_factory=ModifiableValue)
    machine_guns: ModifiableValue = Field(default_factory=ModifiableValue)
    assault_cannons: ModifiableValue = Field(default_factory=ModifiableValue)
    shotguns: ModifiableValue = Field(default_factory=ModifiableValue)
    tasers: ModifiableValue = Field(default_factory=ModifiableValue)


class Influence(ModifiableValue):
    etiquette: ModifiableValue = Field(default_factory=ModifiableValue)
    instruction: ModifiableValue = Field(default_factory=ModifiableValue)
    intimidation: ModifiableValue = Field(default_factory=ModifiableValue)
    leadership: ModifiableValue = Field(default_factory=ModifiableValue)
    negotiation: ModifiableValue = Field(default_factory=ModifiableValue)


class Outdoors(ModifiableValue):
    navigation: ModifiableValue = Field(default_factory=ModifiableValue)
    survival: ModifiableValue = Field(default_factory=ModifiableValue)
    tracking: ModifiableValue = Field(default_factory=ModifiableValue)


class Perception(ModifiableValue):
    visual: ModifiableValue = Field(default_factory=ModifiableValue)
    aural: ModifiableValue = Field(default_factory=ModifiableValue)
    tactile: ModifiableValue = Field(default_factory=ModifiableValue)
    olfactory: ModifiableValue = Field(default_factory=ModifiableValue)
    taste: ModifiableValue = Field(default_factory=ModifiableValue)


class Piloting(ModifiableValue):
    ground_craft: ModifiableValue = Field(default_factory=ModifiableValue)
    aircraft: ModifiableValue = Field(default_factory=ModifiableValue)
    watercraft: ModifiableValue = Field(default_factory=ModifiableValue)


class Sorcery(ModifiableValue):
    counterspelling: ModifiableValue = Field(default_factory=ModifiableValue)
    ritual_spellcasting: ModifiableValue = Field(default_factory=ModifiableValue)
    spellcasting: ModifiableValue = Field(default_factory=ModifiableValue)


class Stealth(ModifiableValue):
    # SR6 GRW 3. Auflage S. 97: Fingerfertigkeit / Schleichen / Tarnung
    # (Verkleiden/"disguise" is a Con specialization, not a Stealth one)
    camouflage: ModifiableValue = Field(default_factory=ModifiableValue)
    palming: ModifiableValue = Field(default_factory=ModifiableValue)
    sneaking: ModifiableValue = Field(default_factory=ModifiableValue)


class Tasking(ModifiableValue):
    compiling: ModifiableValue = Field(default_factory=ModifiableValue)
    decompiling: ModifiableValue = Field(default_factory=ModifiableValue)
    registering: ModifiableValue = Field(default_factory=ModifiableValue)


class Skills(BaseModel):
    astral: Astral = Field(default_factory=Astral)
    athletics: Athletics = Field(default_factory=Athletics)
    biotech: Biotech = Field(default_factory=Biotech)
    close_combat: CloseCombat = Field(default_factory=CloseCombat)
    con: Con = Field(default_factory=Con)
    conjuring: Conjuring = Field(default_factory=Conjuring)
    cracking: Cracking = Field(default_factory=Cracking)
    electronics: Electronics = Field(default_factory=Electronics)
    engineering: Engineering = Field(default_factory=Engineering)
    enchanting: Enchanting = Field(default_factory=Enchanting)
    exotic_weapons: ExoticWeapons = Field(default_factory=ExoticWeapons)
    firearms: Firearms = Field(default_factory=Firearms)
    influence: Influence = Field(default_factory=Influence)
    outdoors: Outdoors = Field(default_factory=Outdoors)
    perception: Perception = Field(default_factory=Perception)
    piloting: Piloting = Field(default_factory=Piloting)
    sorcery: Sorcery = Field(default_factory=Sorcery)
    stealth: Stealth = Field(default_factory=Stealth)
    tasking: Tasking = Field(default_factory=Tasking)


class LimbAttributes(BaseModel):
    body: ModifiableValue = Field(default_factory=ModifiableValue)
    agility: ModifiableValue = Field(default_factory=ModifiableValue)
    reaction: ModifiableValue = Field(default_factory=ModifiableValue)
    strength: ModifiableValue = Field(default_factory=ModifiableValue)


class SR6Character(ModifiableObject):
    type: ObjectType = ObjectType.Character
    gear: GearCollection = Field(default_factory=GearCollection)

    uuid: str
    name: str
    street_name: str
    size: str
    weight: str
    age: str
    gender: Gender
    metatype: Metatype

    attributes: Attributes = Field(default_factory=Attributes)
    skills: Skills = Field(default_factory=Skills)

    physical_initiative_base: ModifiableValue = Field(default_factory=ModifiableValue)
    physical_initiative_dices: ModifiableValue = Field(default_factory=ModifiableValue)
    astral_initiative_base: ModifiableValue = Field(default_factory=ModifiableValue)
    astral_initiative_dices: ModifiableValue = Field(default_factory=ModifiableValue)
    initiative_matrix_ar_base: ModifiableValue = Field(default_factory=ModifiableValue)
    initiative_matrix_ar_dices: ModifiableValue = Field(default_factory=ModifiableValue)
    initiative_matrix_vr_cold_base: ModifiableValue = Field(
        default_factory=ModifiableValue
    )
    initiative_matrix_vr_cold_dices: ModifiableValue = Field(
        default_factory=ModifiableValue
    )
    initiative_matrix_vr_hot_base: ModifiableValue = Field(
        default_factory=ModifiableValue
    )
    initiative_matrix_vr_hot_dices: ModifiableValue = Field(
        default_factory=ModifiableValue
    )

    defense_rating: ModifiableValue = Field(default_factory=ModifiableValue)
    defense_pool_physical: ModifiableValue = Field(default_factory=ModifiableValue)
    defense_astral: ModifiableValue = Field(default_factory=ModifiableValue)
    defense_direct_spell: ModifiableValue = Field(default_factory=ModifiableValue)

    defense_indirect_spell: ModifiableValue = Field(default_factory=ModifiableValue)
    resist_toxin: ModifiableValue = Field(default_factory=ModifiableValue)
    resist_physical_damage: ModifiableValue = Field(default_factory=ModifiableValue)
    resist_astral_damage: ModifiableValue = Field(default_factory=ModifiableValue)
    composure: ModifiableValue = Field(default_factory=ModifiableValue)
    judge_intentions: ModifiableValue = Field(default_factory=ModifiableValue)
    memory: ModifiableValue = Field(default_factory=ModifiableValue)
    lift_carry: ModifiableValue = Field(default_factory=ModifiableValue)

    data_processing: ModifiableValue = Field(default_factory=ModifiableValue)

    physical_condition_monitor: ModifiableValue = Field(default_factory=ModifiableValue)
    stun_condition_monitor: ModifiableValue = Field(default_factory=ModifiableValue)

    right_arm: LimbAttributes = LimbAttributes()
    right_forearm: LimbAttributes = LimbAttributes()
    right_hand: LimbAttributes = LimbAttributes()

    left_arm: LimbAttributes = LimbAttributes()
    left_forearm: LimbAttributes = LimbAttributes()
    left_hand: LimbAttributes = LimbAttributes()

    right_leg: LimbAttributes = LimbAttributes()
    right_lower_leg: LimbAttributes = LimbAttributes()
    right_foot: LimbAttributes = LimbAttributes()

    left_leg: LimbAttributes = LimbAttributes()
    left_lower_leg: LimbAttributes = LimbAttributes()
    left_foot: LimbAttributes = LimbAttributes()

    def __repr__(self):
        return f"<Character>"

    def enable_base_rules(self):
        rules = ALL_RULES.only_rulebooks([Rulebook.SR6Core]).only_modifier_type(
            ModifierType.BASE
        )
        for rule in rules.values():
            self.apply_rule(rule)

    @property
    def current_armor(self) -> Gear:
        armors = self.gear.filter(ObjectType.Armor)
        if armors:
            return armors[0]
        raise NotExistingAttributeError()

    @property
    def weapons(self) -> GearCollection:
        return self.gear.filter(ObjectType.Weapon)

    unarmed: Gear
