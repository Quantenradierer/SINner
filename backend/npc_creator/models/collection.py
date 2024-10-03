import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Collection(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "user")
