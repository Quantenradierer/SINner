import logging
import time

from npc_creator.operations.recreate_image import RecreateImage


from django.core.management.base import BaseCommand

from npc_creator.repositories import npc_repo


class Command(BaseCommand):
    def handle(self, **options):
        logging.info(f"RecreateMissingImages(): Started")
        for npc in npc_repo.requires_image_recreation():
            logging.info(f"RecreateMissingImages: Started for {npc.id}")
            result = RecreateImage(npc).call()
            logging.info(
                f"RecreateMissingImages: Finished for {npc.id} with result {result}"
            )
            time.sleep(60)
