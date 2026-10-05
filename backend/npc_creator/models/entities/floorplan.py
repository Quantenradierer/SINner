from django.db import models

from npc_creator.models import Entity


class FloorplanManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=Entity.Kinds.FLOORPLAN)


class Floorplan(Entity):
    """A generated building plan. It is never edited: other parameters mean a new
    floorplan. `attributes` hold the (validated) request and the floor levels."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = self.Kinds.FLOORPLAN

    class Meta:
        proxy = True

    objects = FloorplanManager()
