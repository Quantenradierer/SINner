import os
from copy import copy
from dataclasses import dataclass

from django.db import models

from npc_creator import config


@dataclass
class AttributeDefinition:
    name: str
    length: int
    reroll: bool


class Npc(models.Model):
    class State(models.TextChoices):
        CREATED = "CR", "Created"
        MODERATED = "MO", "Moderated"
        FAILED = "FA", "Failed"

    state = models.CharField(
        max_length=2,
        choices=State.choices,
        default=State.CREATED,
    )

    user_prompt = models.CharField(max_length=255, blank=True)
    image_generator_description = models.TextField(blank=True)
    default_image_number = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ATTRIBUTE_DEFINITION = [
        AttributeDefinition(name="Beruf", length=0, reroll=True),
        AttributeDefinition(name="Metatyp", length=0, reroll=False),
        AttributeDefinition(name="Ethnizität", length=0, reroll=False),
        AttributeDefinition(name="Geschlecht", length=0, reroll=False),
        AttributeDefinition(name="Alter", length=2, reroll=False),
        AttributeDefinition(name="Catchphrase", length=0, reroll=True),
        AttributeDefinition(name="Detailliertes Aussehen", length=0, reroll=True),
        AttributeDefinition(name="Name", length=0, reroll=True),
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
        AttributeDefinition(name="Konstitution (von 1-6)", length=0, reroll=False),
        AttributeDefinition(name="Geschicklichkeit (von 1-6)", length=0, reroll=False),
        AttributeDefinition(name="Reaktion (von 1-6)", length=0, reroll=False),
        AttributeDefinition(name="Stärke (von 1-6)", length=0, reroll=False),
        AttributeDefinition(name="Willenskraft (von 1-6)", length=0, reroll=False),
        AttributeDefinition(name="Logik (von 1-6)", length=0, reroll=False),
        AttributeDefinition(name="Intuition (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Charisma (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Glück (von 1-6)", length=2, reroll=False),
        AttributeDefinition(name="Magie (von 0-6)", length=2, reroll=False),
        AttributeDefinition(name="Resonanz (von 0-6)", length=2, reroll=False),
    ]

    def __init__(self, *args, **kwargs):
        self.attributes = {}
        attributes = kwargs.pop("attributes", {})
        super(Npc, self).__init__(*args, **kwargs)
        if self.id:
            self.attributes = dict(
                [
                    (attr.key, attr.value)
                    for attr in self.attribute_set.filter(generation=0)
                ]
            )
        self.add_attributes(attributes)

    def save(self, *args, **kwargs):
        super(Npc, self).save(*args, **kwargs)

        attribute_set = self.attribute_set.all()
        attributes_hash = copy(self.attributes)
        for attribute in attribute_set:
            if attribute.key in attributes_hash:
                attribute.value = attributes_hash[attribute.key]
                attribute.save()
                attributes_hash.pop(attribute.key)
            else:
                attribute.delete()

        for key, value in attributes_hash.items():
            attribute = Attribute(key=key, value=value, npc=self)
            attribute.save()

    @property
    def image_objects(self):
        if self.id:
            return self.image_set
        return Npc.objects.none()

    def is_complete(self):
        if len([value for value in self.attributes.values() if value]) < len(
            Npc.ATTRIBUTE_DEFINITION
        ):
            return False
        return True

    def has_image_description(self):
        return bool(self.image_generator_description)

    def __repr__(self):
        return f"<models.Npc id={self.id}>"

    def add_attributes(self, new_attributes):
        existing_attributes = self.attributes
        self.attributes = {}
        for attr_def in Npc.ATTRIBUTE_DEFINITION:
            attr_name = attr_def.name
            value = new_attributes.get(attr_name, "") or existing_attributes.get(
                attr_name, ""
            )
            self.attributes[attr_name] = value


class Attribute(models.Model):
    npc = models.ForeignKey(Npc, on_delete=models.CASCADE, db_index=True)

    key = models.TextField(db_index=True)
    value = models.TextField(db_index=True, blank=True)
    generation = models.IntegerField(default=0)

    def __repr__(self):
        return f"<models.Attribute id={self.id} key={self.key} value={self.value} npc_id={self.npc_id}>"
