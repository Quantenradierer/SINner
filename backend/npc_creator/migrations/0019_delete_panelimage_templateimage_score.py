# Generated by Django 4.1.8 on 2023-10-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0018_move_images_index_again"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PanelImage",
        ),
        migrations.AddField(
            model_name="templateimage",
            name="score",
            field=models.IntegerField(default=200),
        ),
    ]
