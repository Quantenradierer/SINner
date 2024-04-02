# Generated by Django 4.1.13 on 2024-04-02 21:59

from django.db import migrations
from django.db.migrations import RunPython

from npc_creator.models import Npc


def clean_attributes(apps, schema_editor):
    for npc in Npc.objects.all():
        npc.attributes = _clean_attributes(npc, npc.attributes)
        npc.save()


def _clean_attributes(entity, attributes):
    for attr in entity.ATTRIBUTE_DEFINITION:
        if attr.name in attributes and attr.length:
            if type(attributes[attr.name]) is str:
                attributes[attr.name] = attributes[attr.name][: attr.length].strip()
            elif type(attributes[attr.name]) is list:
                attributes[attr.name] = [
                    value[: attr.length].strip() for value in attributes[attr.name]
                ]

    return attributes


class Migration(migrations.Migration):

    dependencies = [
        ("npc_creator", "0042_thumbnails"),
    ]

    operations = [
        migrations.RunPython(clean_attributes, reverse_code=RunPython.noop),
    ]
