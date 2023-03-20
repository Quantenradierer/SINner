from npc_creator.models.npc import Npc


def read_random():
    return Npc.objects.order_by('?').prefetch_related('attribute_set').first()


def find(pk):
    return Npc.objects.prefetch_related('attribute_set').get(pk=pk)


def requires_image_generation():
    return Npc.objects.filter(image_generator_state__eq='', image_url__eq='', image_generator_description__neq='').prefetch_related('attribute_set')


def requires_image_download():
    return Npc.objects.filter(image_generator_state__eq='started', image_url__is=None).prefetch_related('attribute_set')


def create(npc):
    npc.save()
    return npc.id


def delete(npc):
    npc.delete()
    return npc.id


def save(npc):
    npc.save()
    return npc.id
