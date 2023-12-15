from django.db import models


class Feedback(models.Model):
    email = models.CharField(max_length=255, blank=True)
    comment = models.TextField()
