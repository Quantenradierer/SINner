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
        AttributeDefinition(
            name="Konstitution",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6, bei Zwergen 1-7, bei Orks 1-8, bei Trollen 1-9",
        ),
        AttributeDefinition(
            name="Geschicklichkeit",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6, bei Elfen 1-7, bei Trollen 1-5",
        ),
        AttributeDefinition(
            name="Reaktion",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6, bei Zwergen 1-5",
        ),
        AttributeDefinition(
            name="Stärke",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6, bei Zwergen und Orks 1-8, bei Trollen 1-9",
        ),
        AttributeDefinition(
            name="Willenskraft",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6, bei Zwergen 1-7",
        ),
        AttributeDefinition(
            name="Logik",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6",
        ),
        AttributeDefinition(
            name="Intuition",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6",
        ),
        AttributeDefinition(
            name="Charisma",
            length=2,
            reroll=False,
            # additional_data="Bei Menschen und anderen Metatypen normalerweise 1-6, bei Elfen 1-8, bei Orks und Trollen 1-5",
        ),
        AttributeDefinition(
            name="Edge",
            length=2,
            reroll=False,
            additional_data="Int. Bei Menschen 1-7, bei allen anderen Metatypen normalerweise 1-6",
        ),
        AttributeDefinition(
            name="Magie",
            length=2,
            reroll=False,
            additional_data="Int. Normalerweise 0-6. Bei nicht magischen Charakteren 0",
        ),
        AttributeDefinition(
            name="Resonanz",
            length=2,
            reroll=False,
            additional_data="Int. Normalerweise 0-6. Bei nicht Resonanzern 0",
        ),
    ]

    Fill = npc.Fill
    Translate = npc.Translate
    PassImagePrompt = npc.PassImagePrompt
    Check = npc.Check
