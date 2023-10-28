import random

from npc_creator.models.template_image import TemplateImage


def find(keyword):
    try:
        templates = TemplateImage.objects.filter(keyword__exact=keyword)
        weights = [t.score for t in templates]
        return random.choices(templates, weights=weights)[0]
    except IndexError:
        return None


def save(example_image):
    example_image.save()