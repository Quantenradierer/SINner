from django.db import models

from npc_creator.models import Entity
from npc_creator.models.entity import AttributeDefinition
from npc_creator.operations.gpt import npc


class NpcManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=Entity.Kinds.NPC)


class Npc(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = self.Kinds.NPC

    class Meta:
        proxy = True

    objects = NpcManager()

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

    Fill = npc.Fill
    Translate = npc.Translate
    PassImagePrompt = npc.PassImagePrompt
    Check = npc.Check
