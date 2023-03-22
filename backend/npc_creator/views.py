import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models.npc import Npc
from .operations.generate_npc import GenerateNpc
from .repositories import npc_repo


def convert_npc(npc):
    return json.dumps({
        'id': npc.id,
        'image_generator_description': npc.image_generator_description,
        'image_url': npc.image_url,
        'image_generator_state': npc.image_generator_state,
        'attributes': npc.attributes
    })


def read_npc(request, id):
    if id:
        npc = npc_repo.find(id)
    else:
        npc = npc_repo.read_random()
    return HttpResponse(convert_npc(npc))


def random_npc(request):
    npc = npc_repo.read_random()
    return HttpResponse(convert_npc(npc))


def next_npc(request):
    pk = str(request.GET['id'])
    if pk.isdigit():
        npc = npc_repo.next_npc(pk)
    else:
        npc = npc_repo.read_random()
    return HttpResponse(convert_npc(npc))


def prev_npc(request):
    pk = str(request.GET['id'])
    if pk.isdigit():
        npc = npc_repo.prev_npc(pk)
    else:
        npc = npc_repo.read_random()
    return HttpResponse(convert_npc(npc))


@csrf_exempt
def npc(request):
    if request.method == "POST":
        return create_npc(request)
    return HttpResponse(status=405, headers={'Allow', 'POST'})


def create_npc(request):
    data = json.loads(request.body.decode())
    prompt = data.get("prompt")[:255]

    result_npc = GenerateNpc(prompt).call()
    if result_npc:
        npc = result_npc.data
    else:
        npc = Npc(attributes={'Name': result_npc.error})

    return HttpResponse(convert_npc(npc))

