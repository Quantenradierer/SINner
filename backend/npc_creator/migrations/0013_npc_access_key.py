# Generated by Django 4.1.8 on 2023-06-22 12:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('npc_creator', '0012_alter_npc_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='npc',
            name='access_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
