from backend.models.npc import Npc, Attribute


def _split(text):
    lines = text.split('\n')

    image_generator_description = ''
    attributes = {}
    for line in lines:
        if not line.count(':'):
            continue
        key, value = line.split(':')
        if key.strip() in ['Detailliertes Aussehen (english)', 'Detailled Description (English)']:
            image_generator_description = value.strip()
        else:
            attributes[key.strip()] = value.strip()

    return {'image_generator_description': image_generator_description,
            'attributes': attributes}


def fill_npc_from_gpt(npc, gpt_response):
    splitted_response = _split(gpt_response)
    image_generator_description = splitted_response.pop('image_generator_description')

    attributes = list([Attribute(key=key, value=value, npc_id=npc.id) for key, value in splitted_response['attributes'].items()])

    npc.image_generator_description = image_generator_description
    npc.attributes = attributes

