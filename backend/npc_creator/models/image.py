import os
import uuid

from django.db import models
from npc_creator.models import TemplateImage, Npc


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    template = models.ForeignKey(TemplateImage, null=True, on_delete=models.SET_NULL)
    npc = models.ForeignKey(Npc, null=True, on_delete=models.SET_NULL)

    def upvote(self):
        self.score += 1

    def downvote(self):
        self.score -= 1