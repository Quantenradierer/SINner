import uuid

from django.db import models


class Favorite(models.Model):
    entity = models.ForeignKey("Entity", on_delete=models.CASCADE)
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE)
