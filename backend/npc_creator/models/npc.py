import os
from copy import copy
from dataclasses import dataclass

from django.db import models


@dataclass
class AttributeDefinition:
    name: str
    length: int
    reroll: bool


class GenerationBase(models.Model):
    ATTRIBUTE_DEFINITION = []

    image_generator_description = models.TextField(blank=True)
    attributes = models.JSONField(blank=False, null=False, default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def image_objects(self):
        if self.id:
            return self.image_set
        return self.__class__.objects.none()

    def is_complete(self):
        if len([value for value in self.primary_values.values() if value]) < len(
            self.ATTRIBUTE_DEFINITION
        ):
            return False
        return True

    def has_image_description(self):
        return bool(self.image_generator_description)

    def __repr__(self):
        return f"<models.{self.__class__} id={self.id}>"

    @property
    def primary_values(self):
        return dict((key, values[0] if values else '') for key, values in self.attributes.items())

    @property
    def attribute_names(self):
        return [attr_def.name for attr_def in self.ATTRIBUTE_DEFINITION]

    def add_values(self, new_values):
        for key, values in new_values.items():
            if key not in self.attribute_names:
                raise ValueError(f'key {key} not in {self.__class__} ATTRIBUTE_DEFINITIONS')

            self.attributes[key] = self.attributes.get(key, list())
            if type(values) == str:
                values = [values]
            self.attributes[key].extend(values)

    @property
    def attribute_definition(self):
        result = {}
        for attr_def in self.ATTRIBUTE_DEFINITION:
            result[attr_def.name] = {
                'length': attr_def.length,
                'reroll': attr_def.reroll
             }
        return result

class Npc(GenerationBase):
    ATTRIBUTE_DEFINITION = [
        AttributeDefinition(name="Beruf", length=0, reroll=True),
        AttributeDefinition(name="Metatyp", length=50, reroll=False),
        AttributeDefinition(name="Ethnizität", length=0, reroll=False),
        AttributeDefinition(name="Geschlecht", length=0, reroll=False),
        AttributeDefinition(name="Alter", length=10, reroll=False),
        AttributeDefinition(name="Catchphrase", length=0, reroll=True),
        AttributeDefinition(name="Detailliertes Aussehen", length=0, reroll=True),
        AttributeDefinition(name="Name", length=100, reroll=True),
        AttributeDefinition(name="Hintergrundgeschichte", length=0, reroll=True),
        AttributeDefinition(name="Erfahrungen", length=0, reroll=True),
        AttributeDefinition(name="Ressentiments", length=0, reroll=True),
        AttributeDefinition(name="Motivationen", length=0, reroll=True),
        AttributeDefinition(name="Ziele", length=0, reroll=True),
        AttributeDefinition(name="Stärken", length=0, reroll=True),
        AttributeDefinition(name="Schwächen", length=0, reroll=True),
        AttributeDefinition(name="Fertigkeiten", length=0, reroll=True),
        AttributeDefinition(name="Ausrüstung", length=0, reroll=True),
        AttributeDefinition(name="Hobbys und Interessen", length=0, reroll=True),
        AttributeDefinition(name="Eigenarten", length=0, reroll=True),
        AttributeDefinition(name="Familie", length=0, reroll=True),
        AttributeDefinition(name="Kontakte", length=0, reroll=True),
        AttributeDefinition(name="Lootbare Gegenstände", length=0, reroll=True),
        AttributeDefinition(name="Geheimnis", length=0, reroll=False),
        AttributeDefinition(name="Konstitution (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Geschicklichkeit (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Reaktion (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Stärke (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Willenskraft (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Logik (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Intuition (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Charisma (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Glück (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Magie (von 0-6)", length=2, reroll=False),
        AttributeDefinition(name="Resonanz (von 0-6)", length=2, reroll=False),
    ]

