# Generated by Django 4.1.8 on 2023-11-11 16:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0034_alter_npc_attributes_delete_attribute"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Npc",
            new_name="Entity",
        ),
    ]
