from npc_creator.models.entities.npc import Npc


def read_random():
    return Npc.objects.order_by("?").first()
