# Generated by Django 4.1.8 on 2023-10-21 09:27

from django.db import migrations, models
import django.db.models.deletion

from npc_creator import config
from npc_creator.models import Npc
import os

from npc_creator.models.image import Image


def image_structure(*args, **kwargs):
    npcs = Npc.objects.all()
    for npc in npcs:
        for image_name in npc.images:
            Image.objects.create(npc=npc, name=image_name)


class Migration(migrations.Migration):
    dependencies = [
        ('npc_creator', '0023_remove_npc_image_url_image_name'),
    ]

    operations = [
       migrations.RunPython(image_structure),
    ]