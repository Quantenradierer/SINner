# Generated by Django 4.1.7 on 2023-04-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0006_rename_exampleimage_templateimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="npc",
            name="state",
            field=models.CharField(
                choices=[("CR", "Created"), ("MO", "Moderated")],
                default="CR",
                max_length=2,
            ),
        ),
    ]
