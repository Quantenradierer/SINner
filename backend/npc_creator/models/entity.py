import uuid
from dataclasses import dataclass

from django.apps import apps
from django.db import models


@dataclass
class AttributeDefinition:
    name: str
    length: int
    additional_data: str = ""
    optional: bool = False
    type: str = "string"


class Entity(models.Model):
    class Kinds(models.TextChoices):
        NPC = "Npc", "Npc"
        LOCATION = "Location", "Location"
        CUSTOM = "Custom", "Custom"
        CRITTER = "Critter", "Critter"
        VEHICLE = "Vehicle", "Vehicle"
        OBJECTS = "Objects", "Objects"

    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    kind = models.CharField(max_length=20, choices=Kinds.choices)

    image_generator_description = models.TextField(blank=True)
    attributes = models.JSONField(blank=False, null=False, default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ATTRIBUTE_DEFINITION = []
    Fill = None
    Translate = None
    PassImagePrompt = None
    SpecialMidjourneyPrompt = None
    Check = None

    @property
    def instance(self):
        for cls in self.__class__.__subclasses__():
            if cls.__name__ == self.kind:
                return cls.objects.get(pk=self.pk)
        return self

    @property
    def image_objects(self):
        if self.id:
            return self.image_set
        return self.__class__.objects.none()

    @property
    def values(self):
        return self.attributes

    def is_complete(self):
        for attr_def in self.ATTRIBUTE_DEFINITION:
            if attr_def.optional:
                continue

            value = self.primary_values.get(attr_def.name, "")
            if isinstance(value, str):
                value = value.strip()
                if not value:
                    return False
        return True

    def has_image_description(self):
        return bool(self.image_generator_description)

    def __repr__(self):
        return f"<models.{self.__class__} id={self.id}>"

    @property
    def primary_values(self):
        result = {}
        for attr_def in self.ATTRIBUTE_DEFINITION:
            value = self.attributes.get(attr_def.name, "")
            if value and type(value) is list and attr_def.type != "list":
                value = value[0]
            result[attr_def.name] = value
        return result

    @property
    def attribute_names(self):
        return [attr_def.name for attr_def in self.ATTRIBUTE_DEFINITION]

    def add_values(self, new_values):
        for key, values in new_values.items():
            found_key = next(
                (
                    attr_def.name
                    for attr_def in self.ATTRIBUTE_DEFINITION
                    if attr_def.name.lower() == key.lower()
                ),
                None,
            )

            if not found_key:
                continue

            self.attributes[found_key] = self.attributes.get(found_key, "")
            if isinstance(values, str) and not values.strip():
                continue
            self.attributes[key] = values

    @property
    def attribute_definition(self):
        result = {}
        for attr_def in self.ATTRIBUTE_DEFINITION:
            result[attr_def.name] = {
                "length": attr_def.length,
                "reroll": attr_def.reroll,
            }
        return result
