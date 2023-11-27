from dataclasses import dataclass

from django.apps import apps
from django.db import models


@dataclass
class AttributeDefinition:
    name: str
    length: int
    reroll: bool
    additional_data: str = ""
    optional: bool = False


class Entity(models.Model):
    class Kinds(models.TextChoices):
        NPC = "Npc", "Npc"
        LOCATION = "Location", "Location"
        CUSTOM = "Custom", "Custom"
        CRITTER = "Critter", "Critter"
        VEHICLE = "Vehicle", "Vehicle"

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

            if not self.primary_values.get(attr_def.name, "").strip():
                return False
        return True

    def has_image_description(self):
        return bool(self.image_generator_description)

    def __repr__(self):
        return f"<models.{self.__class__} id={self.id}>"

    @property
    def primary_values(self):
        return dict(
            (key, values[0] if values else "")
            for key, values in self.attributes.items()
        )

    @property
    def attribute_names(self):
        return [attr_def.name for attr_def in self.ATTRIBUTE_DEFINITION]

    def add_values(self, new_values):
        for key, values in new_values.items():
            if key not in self.attribute_names:
                continue
                # raise ValueError(
                #    f"key {key} not in {self.__class__} ATTRIBUTE_DEFINITIONS"
                # )

            self.attributes[key] = self.attributes.get(key, list())
            if type(values) == str:
                if not values.strip():
                    continue
                values = [values]
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
