# Generated by Django 4.1.7 on 2023-04-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0007_npc_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attribute",
            name="value",
            field=models.TextField(blank=True, db_index=True),
        ),
    ]
