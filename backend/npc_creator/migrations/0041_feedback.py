# Generated by Django 4.1.8 on 2023-12-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("npc_creator", "0040_custom_alter_entity_kind"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(blank=True, max_length=255)),
                ("comment", models.TextField()),
            ],
        ),
    ]