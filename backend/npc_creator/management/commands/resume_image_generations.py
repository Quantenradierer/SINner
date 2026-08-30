"""Re-drive image generations that are stuck IN_PROGRESS.

The normal retry loop lives in a per-request worker thread, so a process
restart (e.g. a redeploy) orphans any generation still waiting on Midjourney.
This command picks those up, checks the Discord channel for the finished grid
and downloads it. Safe to run repeatedly (e.g. from cron).
"""

import logging

from django.core.management.base import BaseCommand

from npc_creator.jobs.generation_job import advance_generation
from npc_creator.models.image_generation import ImageGeneration


class Command(BaseCommand):
    help = "Download finished images for generations stuck IN_PROGRESS."

    def add_arguments(self, parser):
        parser.add_argument(
            "--id",
            type=int,
            action="append",
            dest="ids",
            help="Only process the given generation id(s). Repeatable.",
        )

    def handle(self, *args, **options):
        generations = ImageGeneration.objects.filter(
            state=ImageGeneration.State.IN_PROGRESS
        )
        if options.get("ids"):
            generations = generations.filter(pk__in=options["ids"])

        generations = list(generations.order_by("id"))
        if not generations:
            self.stdout.write("no generations IN_PROGRESS")
            return

        for generation in generations:
            try:
                advance_generation(generation)
            except Exception:
                logging.exception(f"generation {generation.id}: resume failed")
                self.stderr.write(f"generation {generation.id}: error (see log)")
                continue

            generation.refresh_from_db()
            self.stdout.write(f"generation {generation.id}: {generation.state}")
