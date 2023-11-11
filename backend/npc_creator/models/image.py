import os
import uuid

from django.db import models
from npc_creator.models import TemplateImage, Entity
from npc_creator.models.image_generation import ImageGeneration


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    generation = models.ForeignKey(
        ImageGeneration, null=True, on_delete=models.SET_NULL
    )
    npc = models.ForeignKey(Entity, null=True, on_delete=models.SET_NULL)

    @property
    def template(self):
        if self.generation:
            return self.generation.template

    def upvote(self):
        self.score += 1

    def downvote(self):
        self.score -= 1
