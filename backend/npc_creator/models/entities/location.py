
from django.db import models

from npc_creator.models import Entity
from npc_creator.models.entity import AttributeDefinition


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
        AttributeDefinition(name="Beruf", length=0, reroll=True, additional_data="z.B. Bar, Club, Unternehmen, Wohnhaus, Untergrund, etc."),
        AttributeDefinition(name="Aussehen", length=0, reroll=True, additional_data="innen"),
        AttributeDefinition(name="Stadtteil/Zone", length=0, reroll=True, additional_data=""),
        AttributeDefinition(name="Zugehörige Gruppe/Corp/Fraktion", length=0, reroll=True, additional_data="z.B. Shadowrunners, Knight Errant, Ares, Evo, etc."),
        AttributeDefinition(name="Besonderheiten", length=0, reroll=True, additional_data="magische Aktivität, High Tech Ausstattung, Kriminelle Aktivität"),
        AttributeDefinition(name="Diverse Hinweise", length=0, reroll=True, additional_data="z.B. Versteckte Passagen, Hinterhalte, häufige Patrouillen"),
        AttributeDefinition(name="Verfügbarkeit von Sicherheitssystemen", length=0, reroll=True, additional_data="z.B. Kameras, Scheinwerfer, Lasertraps, etc"),
        AttributeDefinition(name="Aktuelle Aktionen/Events", length=0, reroll=True, additional_data="z.B. Anzahl der Mitarbeiter, Gäste, Bewohner, etc."),
        AttributeDefinition(name="Gerüchte und Geschichten über die Location", length=0, reroll=True, additional_data="z.B. Konzerte, Happy Hours, Verkaufsaktionen, etc.")
    ]
