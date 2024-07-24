# Generated by Django 4.1.13 on 2024-07-16 12:59

from django.db import migrations, models
import uuid


def generate_uuids(apps, schema_editor):
    Entity = apps.get_model("npc_creator", "Entity")
    namespace_uuid = uuid.UUID("12345678-1234-5678-1234-567812345678")

    for entity in Entity.objects.all():
        name = str(entity.id)
        entity.temp_id = uuid.uuid5(namespace_uuid, name)
        entity.save()


class Migration(migrations.Migration):

    dependencies = [
        ("npc_creator", "0048_alter_entity_kind"),
    ]

    operations = [
        migrations.AddField(
            model_name="entity",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RunPython(generate_uuids),
    ]