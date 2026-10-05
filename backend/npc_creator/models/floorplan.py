import os

from django.db import models

from npc_creator.models import Entity


class FloorplanGeneration(models.Model):
    """Progress of rendering one floorplan; polled by the frontend."""

    class State(models.TextChoices):
        QUEUED = "queued", "Queued"
        RENDERING = "rendering", "Rendering"
        DONE = "done", "Done"
        FAILED = "failed", "Failed"

    entity = models.OneToOneField(
        Entity, on_delete=models.CASCADE, related_name="floorplan_generation"
    )
    state = models.CharField(
        max_length=10, choices=State.choices, default=State.QUEUED
    )
    steps_done = models.PositiveSmallIntegerField(default=0)
    steps_total = models.PositiveSmallIntegerField(default=0)
    error = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def floorplan_file_upload_to(instance: "FloorplanFile", filename: str) -> str:
    stem = filename.split(".")[0]
    return os.path.join("floorplans", stem[:2], stem[2:4], filename)


class FloorplanFile(models.Model):
    """A generated file of a floorplan. `level` is the floor (negative: basement) and
    None for files that cover the whole building."""

    class Kind(models.TextChoices):
        DD2VTT = "dd2vtt", "Universal VTT"
        BUILDING = "building", "Building JSON"

    entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, related_name="floorplan_files"
    )
    kind = models.CharField(max_length=10, choices=Kind.choices)
    level = models.SmallIntegerField(null=True)
    file = models.FileField(upload_to=floorplan_file_upload_to)

    created_at = models.DateTimeField(auto_now_add=True)
