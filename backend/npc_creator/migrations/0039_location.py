# Generated by Django 4.1.8 on 2023-11-15 18:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0038_rename_npc_image_entity_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("npc_creator.entity",),
        ),
    ]
