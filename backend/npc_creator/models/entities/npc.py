from typing import Annotated

from django.db import models
from pydantic import constr, BaseModel, Field

from npc_creator.game_mechanics.named_list_with_mods import MinimalGear
from npc_creator.game_mechanics.sr6.character import Metatype, Gender
from npc_creator.models import Entity
from npc_creator.operations.gpt import npc


class NpcManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=Entity.Kinds.NPC)


class GalleryAttributes(BaseModel):
    profession: str
    metatype_enum: Metatype = Field(
        description=f"available metatypes: {', '.join([m.value for m in Metatype])}"
    )
    ethnicity: str
    age: Annotated[str, Field(max_length=10)]
    gender: constr(max_length=20)
    gender_enum: Gender = Field(
        description=f"available genders {', '.join([m.value for m in Gender])}"
    )
    appearance: str


class StoryAttributes(BaseModel):
    profession: str
    metatype: constr(max_length=50)
    metatype_enum: Metatype = Field(
        description=f"available metatypes: {', '.join([m.value for m in Metatype])}"
    )
    ethnicity: str
    gender: constr(max_length=50)
    gender_enum: Gender = Field(
        description=f"available genders {', '.join([m.value for m in Gender])}"
    )
    age: constr(max_length=10)
    catchphrase: str
    appearance: str
    name: constr(max_length=100)
    backstory: str
    experiences: str
    resentments: str
    motivations: str
    strengths: str
    weaknesses: str
    hobbies_and_interests: str
    quirks: str
    family: str
    contacts: str = Field(
        ...,
        description="A text which describes the npcs personal and/or business contacts. NOT A JSON LIST",
    )
    secret: str


class SR6Attributes(BaseModel):
    constitution: int = Field(
        ...,
        description="Integer",
    )
    agility: int = Field(
        ...,
        # description="For humans and other metatypes normally 1-6, for elves 1-7, for trolls 1-5",
    )
    reaction: int = Field(
        ...,
        # description="For humans and other metatypes normally 1-6, for dwarves 1-5",
    )
    strength: int = Field(
        ...,
        # description="For humans and other metatypes normally 1-6, for dwarves and orks 1-8, for trolls 1-9",
    )
    willpower: int = Field(
        ...,
        # description="For humans and other metatypes normally 1-6, for dwarves 1-7",
    )
    logic: int = Field(
        ...,
        # description="For humans and other metatypes normally 1-6"
    )
    intuition: int = Field(
        ...,
        # description="For humans and other metatypes normally 1-6"
    )
    charisma: int = Field(
        ...,
        # description="For humans and other metatypes normally 1-6, for elves 1-8, for orks and trolls 1-5",
    )
    edge: int = Field(
        ...,
        # description="For humans 1-7, for all other metatypes normally 1-6",
    )
    magic: int = Field(
        ...,
        description="For magical characters normally 0-6. For non-magical characters 0",
    )
    resonance: int = Field(
        ...,
        description="For resonant characters normally 0-6. For non-resonant characters 0",
    )

    skill_astral: int
    skill_athletics: int
    skill_biotech: int
    skill_close_combat: int
    skill_con: int
    skill_conjuring: int
    skill_cracking: int
    skill_electronics: int
    skill_enchanting: int
    skill_engineering: int
    skill_exotic_weapons: int
    skill_firearms: int
    skill_influence: int
    skill_outdoors: int
    skill_perception: int
    skill_piloting: int
    skill_sorcery: int
    skill_stealth: int
    skill_tasking: int = Field(
        ...,
        description="For non-resonant characters 0",
    )


class SR6Equipment(BaseModel):
    #equipment: str = Field(..., description="String. Comma separated list of equipment")
    equipment: list[MinimalGear] = Field(
        ..., description="Fill this if empty. See equipment list for ids and structure"
    )
    """
    weapon_ids: list[str] = Field(
        ...,
        description='list of IDs from the weapons list, e.g. ["weapon_id_1", "weapon_id_2"]',
    )
    armor_ids: list[str] = Field(
        ...,
        description='list of IDs from the armor list. Maximum 1 of each subtype. e.g. ["armor_id_1", "helmet_id_2"]',
    )
    """


class Npc(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = self.Kinds.NPC

    class Meta:
        proxy = True

    objects = NpcManager()

    SCHEMAS = {
        "default": StoryAttributes,
        "sr6": SR6Attributes,
        "sr6equipment": SR6Equipment,
        "gallery": GalleryAttributes,
    }

    Fill = npc.Fill
    Translate = npc.Translate
    PassImagePrompt = npc.PassImagePrompt
    Check = npc.Check
    Export = npc.Export
