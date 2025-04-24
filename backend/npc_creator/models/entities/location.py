from django.db import models
from pydantic import BaseModel, Field

from npc_creator.models import Entity
from npc_creator.operations.gpt import location, entity


class GalleryAttributes(BaseModel):
    appearance: str


class LocationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=Entity.Kinds.LOCATION)


class LocationAttributes(BaseModel):
    appearance: str
    name: str
    type: str = Field(
        ..., description="e.g., Bar, Club, Company, Residence, Underground, etc."
    )
    special_features: str = Field(
        ..., description="magical activity, high-tech equipment, criminal activity"
    )
    remarks: str = Field(
        ..., description="e.g., hidden passages, ambushes, frequent patrols"
    )
    security_systems: str = Field(
        ..., description="e.g., cameras, spotlights, laser traps, etc."
    )
    events: str = Field(
        ..., description="e.g., number of employees, guests, residents, etc."
    )
    rumors_and_stories: str = Field(
        ..., description="e.g., concerts, happy hours, sales promotions, etc."
    )
    reviews: list[dict[str, str]]


class Location(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = self.Kinds.LOCATION

    class Meta:
        proxy = True

    objects = LocationManager()

    SCHEMAS = {
        "default": LocationAttributes,
        "gallery": GalleryAttributes,
    }

    Fill = location.Fill
    Translate = location.Translate
    PassImagePrompt = location.PassImagePrompt
    Check = entity.Check
    Export = entity.Export
