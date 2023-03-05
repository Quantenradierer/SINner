from models.npc import Attribute


def dict_from_text(text):
    lines = text.split('\n')

    attributes = {}
    for line in lines:
        if not line.count(':'):
            continue
        key, value = line.split(':')

        attributes[key.strip()] = value.strip()

    return attributes
