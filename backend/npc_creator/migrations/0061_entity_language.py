from django.db import migrations, models


def set_floorplan_language(apps, schema_editor):
    """Everything else was created in German; floorplans stored their language."""
    Entity = apps.get_model("npc_creator", "Entity")
    for entity in Entity.objects.filter(kind="Floorplan").iterator():
        language = (entity.attributes or {}).get("language")
        if language == "en":
            entity.language = "en"
            entity.save(update_fields=["language"])


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0060_floorplan"),
    ]

    operations = [
        migrations.AddField(
            model_name="entity",
            name="language",
            field=models.CharField(
                choices=[("de", "Deutsch"), ("en", "English")],
                db_index=True,
                default="de",
                max_length=2,
            ),
        ),
        migrations.RunPython(set_floorplan_language, migrations.RunPython.noop),
    ]
