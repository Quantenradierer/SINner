# Generated by Django 4.1.8 on 2023-10-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npc_creator', '0021_remove_image_name_alter_image_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]