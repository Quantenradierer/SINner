import uuid

from django.db import models


class Favorite(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entity = models.ForeignKey("Entity", on_delete=models.CASCADE)
    collection = models.ForeignKey(
        "Collection", on_delete=models.CASCADE, related_name="favorites"
    )

    class Meta:
        unique_together = ("entity", "collection")
