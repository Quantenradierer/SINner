from django.db import models

from npc_creator.models import Entity
from npc_creator.models.entity import AttributeDefinition
from npc_creator.operations.gpt import custom


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

    ATTRIBUTE_DEFINITION = [
        AttributeDefinition(name="Aussehen", length=0, additional_data="innen"),
        AttributeDefinition(
            name="Parameter", length=0, additional_data="", optional=True
        ),
    ]
    Fill = custom.Fill
    Translate = custom.Translate
    PassImagePrompt = custom.PassImagePrompt
    Check = custom.Check
