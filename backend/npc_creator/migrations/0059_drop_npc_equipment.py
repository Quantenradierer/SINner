"""Drop the stored ``equipment`` value from every NPC.

Historically ``equipment`` was filled as free prose ("Cyberdeck, VR-Headset,
Tablet") or, more recently, an unreliable list that mixed real gear ids with
hallucinated ones. The Foundry export needs a clean list of resolvable gear
ids, and ``schema_complete`` only checks key *presence* -- so a stale prose
value would never be refilled.

Removing the key makes the ``sr6equipment`` schema incomplete again, so the
next full sheet fill / export re-runs the equipment fill from scratch. This is
a one-way migration: the old prose descriptions are not recoverable.
"""

from django.db import migrations


def drop_equipment(apps, schema_editor):
    Entity = apps.get_model("npc_creator", "Entity")
    for entity in Entity.objects.filter(kind="Npc").iterator():
        attributes = entity.attributes or {}
        if "equipment" in attributes:
            attributes.pop("equipment")
            entity.attributes = attributes
            entity.save(update_fields=["attributes"])


class Migration(migrations.Migration):

    dependencies = [
        ("npc_creator", "0058_image_file_image_thumbnail"),
    ]

    operations = [
        migrations.RunPython(drop_equipment, migrations.RunPython.noop),
    ]
