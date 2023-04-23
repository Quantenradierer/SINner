import os
from copy import copy

from django.db import models

from npc_creator import config


class PanelImage(models.Model):
    description = models.CharField(max_length=255, blank=True)
    panel_name = models.CharField(max_length=255, unique=True)
