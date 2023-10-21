# Generated by Django 4.1.8 on 2023-10-21 09:27

from django.db import migrations, models
import django.db.models.deletion

from npc_creator import config
from npc_creator.models import Npc
import os


def image_structure(*args, **kwargs):
    npcs = Npc.objects.all()
    for npc in npcs:
        npc.default_image_number = max(0, npc.default_image_number) - 1
        npc.save()


class Migration(migrations.Migration):
    dependencies = [
        ('npc_creator', '0016_move_images'),
    ]

    operations = [
       migrations.RunPython(image_structure),
    ]