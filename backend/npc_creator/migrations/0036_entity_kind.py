# Generated by Django 4.1.8 on 2023-11-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0035_rename_npc_entity"),
    ]

    operations = [
        migrations.AddField(
            model_name="entity",
            name="kind",
            field=models.CharField(
                choices=[
                    ("NPC", "NPC"),
                    ("LOCATION", "LOCATION"),
                    ("CRITTER", "CRITTER"),
                ],
                default="NPC",
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]