# Generated by Django 4.1.8 on 2023-11-12 00:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0037_npc"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image",
            old_name="npc",
            new_name="entity",
        ),
        migrations.RenameField(
            model_name="imagegeneration",
            old_name="npc",
            new_name="entity",
        ),
    ]
