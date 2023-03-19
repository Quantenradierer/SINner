from django.http import HttpResponse

from .models.npc import Npc
from .operations.generate_npc import GenerateNpc
from .repositories import npc_repo


def convert_npc(npc):
    attributes_dict = {}
    for attribute in npc.attributes:
        attributes_dict[attribute.key] = attribute.value

    npc_dict = {c.name: getattr(npc, c.name) for c in npc.__table__.columns}
    return {**npc_dict, **{'attributes': attributes_dict}}


def read_npc(request):
    id = None
    if id and id.isdigit():
        npc = npc_repo.find(id)
    else:
        npc = npc_repo.read_random()

    return convert_npc(npc)


def create_npc(request):
    prompt = request.json['prompt'][:255]

    result_npc = GenerateNpc(prompt).call()
    if result_npc:
        npc = result_npc.data
    else:
        npc = Npc(id='error', attributes={'Name': result_npc.error})

    return convert_npc(npc)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
