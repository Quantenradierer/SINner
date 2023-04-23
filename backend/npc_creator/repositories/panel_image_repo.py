from npc_creator.models.panel_image import PanelImage


def exists(panel_name):
    return PanelImage.objects.filter(panel_name__exact=panel_name).exists()


def save(panel_image):
    panel_image.save()
    return panel_image.id


def find_description(description):
    return PanelImage.objects.filter(description__icontains=description).first()
