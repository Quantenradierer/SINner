import uuid
from dataclasses import dataclass

from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import models


class Entity(models.Model):
    class Kinds(models.TextChoices):
        NPC = "Npc", "Npc"
        LOCATION = "Location", "Location"
        CUSTOM = "Custom", "Custom"
        CRITTER = "Critter", "Critter"
        VEHICLE = "Vehicle", "Vehicle"
        OBJECTS = "Objects", "Objects"

    class States(models.TextChoices):
        UNPUBLISHED = "Unpublished", "Unpublished"
        PRIVATE = "Private", "Private"
        PUBLISHED = "Published", "Published"

    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    kind = models.CharField(max_length=20, choices=Kinds.choices)
    state = models.CharField(
        max_length=20, choices=States.choices, default=States.UNPUBLISHED
    )

    prompt = models.TextField(blank=True)
    image_generator_description = models.TextField(blank=True)
    attributes = models.JSONField(blank=False, null=False, default=dict)
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="entities",
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    SCHEMAS = []
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

    def schema_complete(self, schema_name):
        schema = self.SCHEMAS[schema_name]

        return all(name in self.attributes for name in schema.__fields__.keys())

    def has_image_description(self):
        return bool(self.image_generator_description)

    def __repr__(self):
        return f"<models.{self.__class__} id={self.id}>"

    def add_values(self, new_values):
        for name, values in new_values.items():
            found_key = next(
                (
                    def_name
                    for def_name in self.attribute_defintions.keys()
                    if def_name.lower() == name.lower()
                ),
                None,
            )

            if not found_key:
                continue

            self.attributes[found_key] = self.attributes.get(found_key, "")
            if isinstance(values, str) and not values.strip():
                continue
            self.attributes[name] = values

    @property
    def attribute_defintions(self):
        result = {}
        for schemas in self.SCHEMAS.values():
            for name, attr in schemas.__fields__.items():
                result[name] = attr
        return result
