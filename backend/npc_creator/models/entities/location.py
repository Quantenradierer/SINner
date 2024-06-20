from django.db import models

from npc_creator.models import Entity
from npc_creator.models.entity import AttributeDefinition
from npc_creator.operations.gpt import location, entity


class LocationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=Entity.Kinds.LOCATION)


class Location(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = self.Kinds.LOCATION

    class Meta:
        proxy = True

    objects = LocationManager()

    ATTRIBUTE_DEFINITION = [
        AttributeDefinition(
            name="Aussehen", length=0, reroll=True, additional_data="innen"
        ),
        AttributeDefinition(name="Name", length=0, reroll=True, additional_data=""),
        AttributeDefinition(
            name="Typ",
            length=0,
            reroll=True,
            additional_data="z.B. Bar, Club, Unternehmen, Wohnhaus, Untergrund, etc.",
        ),
        AttributeDefinition(
            name="Besonderheiten",
            length=0,
            reroll=True,
            additional_data="magische Aktivität, High Tech Ausstattung, Kriminelle Aktivität",
        ),
        AttributeDefinition(
            name="Hinweise",
            length=0,
            reroll=True,
            additional_data="z.B. Versteckte Passagen, Hinterhalte, häufige Patrouillen",
        ),
        AttributeDefinition(
            name="Verfügbarkeit von Sicherheitssystemen",
            length=0,
            reroll=True,
            additional_data="z.B. Kameras, Scheinwerfer, Lasertraps, etc",
        ),
        AttributeDefinition(
            name="Aktuelle Aktionen/Events",
            length=0,
            reroll=True,
            additional_data="z.B. Anzahl der Mitarbeiter, Gäste, Bewohner, etc.",
        ),
        AttributeDefinition(
            name="Gerüchte und Geschichten über die Location",
            length=0,
            reroll=True,
            additional_data="z.B. Konzerte, Happy Hours, Verkaufsaktionen, etc.",
        ),
        AttributeDefinition(
            name="Bewertungen",
            length=0,
            reroll=True,
            additional_data="",
            type="list",
        ),
    ]
    Fill = location.Fill
    Translate = location.Translate
    PassImagePrompt = location.PassImagePrompt
    Check = entity.Check
