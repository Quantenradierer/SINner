from npc_creator.operations.recreate_image import RecreateImage




from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        RecreateImage()
