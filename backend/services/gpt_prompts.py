from collections import ChainMap
from copy import copy

import config
from config import PROMPT


def create_npc_prompt(user_prompt, npc, attributes):
    existing_attributes = ''
    missing_attributes = ''

    flat_attributes = copy(attributes)

    for attribute in npc.attributes:
        flat_attributes[attribute.key] = attribute.value

    for item in flat_attributes.items():
        value = item[1] or ''
        if value:
            existing_attributes += f'{item[0]}: {value}\n'
        else:
            missing_attributes += f'{item[0]}: {value}\n'

    return PROMPT.format(user_prompt=user_prompt,
                         existing_attributes=existing_attributes,
                         missing_attributes=missing_attributes)


def translate_appearance_prompt(text):
    return config.TRANSLATE_PROMPT.format(text=text)