from npc_creator.models.template_image import TemplateImage


def find(keyword):
    try:
        return TemplateImage.objects.filter(keyword__exact=keyword).order_by('?').first()
    except IndexError:
        return None


def save(example_image):
    example_image.save()