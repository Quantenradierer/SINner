# Generated by Django 4.1.8 on 2023-11-10 21:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0031_remove_npc_default_image_number_remove_npc_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="npc",
            name="user_prompt",
        ),
    ]
