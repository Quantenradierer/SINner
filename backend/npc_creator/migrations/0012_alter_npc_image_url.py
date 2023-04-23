# Generated by Django 4.1.8 on 2023-04-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npc_creator', '0011_image_number_as_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='image_url',
            field=models.CharField(blank=True, default='pk-{pk}_counter-{counter}.png', max_length=255),
        ),
    ]
