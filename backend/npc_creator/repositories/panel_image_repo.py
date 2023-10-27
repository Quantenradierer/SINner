from npc_creator.models.image import PanelImage


def save(panel_image):
    panel_image.save()
    return panel_image.id


def find_description(description):
    return PanelImage.objects.filter(description__icontains=description).first()
