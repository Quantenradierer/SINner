# Generated by Django 4.1.13 on 2024-07-18 10:29

from django.db import migrations

TRANLSATION_DICT = {
    "Beruf": "profession",
    "Metatyp": "metatype",
    "Ethnizität": "ethnicity",
    "Geschlecht": "gender",
    "Alter": "age",
    "Catchphrase": "catchphrase",
    "Detailliertes Aussehen": "appearance",
    "Name": "name",
    "Hintergrundgeschichte": "backstory",
    "Erfahrungen": "experiences",
    "Ressentiments": "resentments",
    "Motivationen": "motivations",
    "Stärken": "strengths",
    "Schwächen": "weaknesses",
    "Hobbys und Interessen": "hobbies_and_interests",
    "Eigenarten": "quirks",
    "Familie": "family",
    "Kontakte": "contacts",
    "Geheimnis": "secret",
    "Fertigkeiten": "skills",
    "Ausrüstung": "equipment",
    "Lootbare Gegenstände": "lootable_items",
    "Konstitution": "constitution",
    "Geschicklichkeit": "agility",
    "Reaktion": "reaction",
    "Stärke": "strength",
    "Willenskraft": "willpower",
    "Logik": "logic",
    "Intuition": "intuition",
    "Charisma": "charisma",
    "Edge": "edge",
    "Magie": "magic",
    "Resonanz": "resonance",
    # location
    "Aussehen": "appearance",
    "Name": "name",
    "Typ": "type",
    "Besonderheiten": "special_features",
    "Hinweise": "remarks",
    "Verfügbarkeit von Sicherheitssystemen": "security_systems",
    "Aktuelle Aktionen/Events": "events",
    "Gerüchte und Geschichten über die Location": "rumors_stories",
    "Bewertungen": "reviews",
    # custom
    "Aussehen": "appearance",
    "Parameter": "parameter",
}


def translate_attribute_keys(apps, schema_editor):
    Entity = apps.get_model("npc_creator", "Entity")
    for entity in Entity.objects.all():
        entity.attributes = {
            TRANLSATION_DICT.get(key, key): value
            for key, value in entity.attributes.items()
        }
        entity.save()


class Migration(migrations.Migration):

    dependencies = [
        ("npc_creator", "0051_entity_prompt"),
    ]

    operations = [
        migrations.RunPython(
            translate_attribute_keys, reverse_code=migrations.RunPython.noop
        )
    ]
