from backend.repositories.npc import Npc, Attribute


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


def npc_from_gpt(gpt_response):
    splitted_response = _split(gpt_response)
    image_generator_description = splitted_response.pop('image_generator_description')

    attributes = list([Attribute(key=key, value=value) for key, value in splitted_response['attributes'].items()])
    print(attributes[0].key, attributes[0].value)
    return Npc(image_generator_description=image_generator_description, attributes=attributes)

