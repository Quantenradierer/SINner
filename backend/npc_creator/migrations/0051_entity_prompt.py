# Generated by Django 4.1.13 on 2024-07-17 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("npc_creator", "0050_alter_entity_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="entity",
            name="prompt",
            field=models.TextField(blank=True),
        ),
    ]