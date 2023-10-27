
from django.db import models

from npc_creator.models import Npc, TemplateImage


class ImageGeneration(models.Model):
    class State(models.TextChoices):
        CREATED = 'CR', 'Created'
        IN_PROGRESS = 'IN', 'In Progress'
        DOWNLOADED = 'DL', 'Downloaded'
        FAILED = 'FA', 'Failed'
        DONE = 'DO', 'Done'

    state = models.CharField(
        max_length=2,
        choices=State.choices,
        default=State.CREATED,
    )

    template = models.ForeignKey(TemplateImage, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    retry_count = models.IntegerField(default=0)
    url = models.CharField(max_length=256)
    npc = models.ForeignKey(Npc, on_delete=models.CASCADE, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
