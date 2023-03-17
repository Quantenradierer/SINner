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
    if not missing_attributes:
        return None

    return PROMPT.format(user_prompt=user_prompt,
                         existing_attributes=existing_attributes,
                         missing_attributes=missing_attributes)


def translate_appearance_prompt(npc):
    return config.TRANSLATE_PROMPT.format(
        metatyp=npc.get_attribute('Metatyp'),
        beruf=npc.get_attribute('Beruf'),
        image_generator_description=npc.get_attribute(config.VISUAL_APPEARANCE_ATTRIBUTE)
    )
