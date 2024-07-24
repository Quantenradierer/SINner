from django.db import models
from pydantic import BaseModel, Field

from npc_creator.models import Entity
from npc_creator.models.entity import AttributeDefinition
from npc_creator.operations.gpt import custom


class CustomAttributes(BaseModel):
    appearance: str = Field(...)
    parameter: str


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=Entity.Kinds.CUSTOM)


class Custom(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = self.Kinds.CUSTOM

    class Meta:
        proxy = True

    objects = CustomManager()

    SCHEMAS = {"default": CustomAttributes}
    Fill = custom.Fill
    Translate = custom.Translate
    PassImagePrompt = custom.PassImagePrompt
    Check = custom.Check
