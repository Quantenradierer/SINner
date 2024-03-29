from django.db import models


class TemplateImage(models.Model):
    """
    Example Images are image urls which can be used by midjourney to create better images.
    Like, it created a good troll once and now we can use this one image and create variations.
    Those variations then can be used to create further variations.
    """

    keyword = models.CharField(max_length=128)
    url = models.CharField(max_length=512)

    score = models.IntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def upvote(self):
        self.score += 1

    def downvote(self):
        self.score = max(0, self.score - 1)
