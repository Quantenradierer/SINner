import os
from copy import copy

from django.db import models
from django.db.models import JSONField

from npc_creator import config


class GptRequest(models.Model):
    class State(models.TextChoices):
        STARTED = 'ST', 'Started'
        COMPLETED = 'CO', 'Completed'
        FAILED = 'FF', 'Failed'

    input = JSONField(blank=False)
    output = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    kind = models.TextField(blank=True)

    state = models.CharField(
        max_length=2,
        choices=State.choices,
        default=State.STARTED,
    )

    def finished(self):
        self.state = GptRequest.State.COMPLETED

    def failed(self):
        self.state = GptRequest.State.FAILED