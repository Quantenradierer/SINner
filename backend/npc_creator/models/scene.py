from django.contrib.auth import get_user_model
from django.db import models

from npc_creator.models import Entity

User = get_user_model()


class Scene(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    entities = models.ManyToManyField(Entity)

