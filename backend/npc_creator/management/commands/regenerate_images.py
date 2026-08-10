import time
import random

from django.core.management.base import BaseCommand, CommandError

from npc_creator.jobs.generation_job import generation_job_async
from npc_creator.models import Npc, ImageGeneration


class Command(BaseCommand):
    help = "Goes to all "

    def handle(self, *args, **options):
        assert Npc.objects.count() == 30  # default database

        for entity in Npc.objects.all():
            entity.image_generator_description = ""
            entity.save()

            generation = ImageGeneration(entity=entity)
            generation.save()
            generation_job_async(generation)

            time.sleep(random.random() + random.randint(10, 20))
