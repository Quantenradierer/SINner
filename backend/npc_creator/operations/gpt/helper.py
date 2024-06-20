import json

from npc_creator import config
from npc_creator.models import Entity


def entity_prompt(entity):
    result = ""
    values = entity.primary_values
    for attribute_definition in entity.ATTRIBUTE_DEFINITION:
        key = attribute_definition.name
        result += f'"{key}": {json.dumps(values[key])} // {attribute_definition.additional_data}\n'

    return [
        f"{{\n{result}\n}}",
    ]
