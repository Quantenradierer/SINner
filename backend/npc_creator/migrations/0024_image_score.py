# Generated by Django 4.1.8 on 2023-10-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0023_remove_npc_image_url_image_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]
