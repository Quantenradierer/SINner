# Generated by Django 4.1.13 on 2024-06-22 23:51


from django.db.migrations import RunPython

from npc_creator.models import Entity
from django.conf import settings
from django.db import migrations


def convert_attributes(apps, schema_editor):
    for npc in Entity.objects.all():
        for key, value in npc.attributes.items():
            if (isinstance(value, list) or isinstance(value, tuple)) and len(
                value
            ) == 1:
                npc.attributes[key] = value[0]

        npc.save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("npc_creator", "0046_favorite_collection"),
    ]

    operations = [
        migrations.RunPython(convert_attributes, reverse_code=RunPython.noop),
    ]
