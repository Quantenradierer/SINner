from copy import copy

from npc_creator import config


def create_npc_prompt(user_prompt, npc_attributes, attributes):
    attributes = copy(attributes)
    existing_attributes = []
    missing_attributes = []

    for key, value in npc_attributes.items():
        if value:
            attributes[key] = value

    for key, value in attributes.items():
        value = value or ''
        if value:
            existing_attributes += f'{key}: {value}\n'
        else:
            missing_attributes += f'{key}: \n'

    if not missing_attributes:
        return None

    return config.PROMPT.format(user_prompt=user_prompt,
                                existing_attributes=existing_attributes,
                                missing_attributes=missing_attributes)


def translate_appearance_prompt(npc):
    return config.TRANSLATE_PROMPT.format(
        metatyp=npc.attributes.get('Metatyp', ''),
        beruf=npc.attributes.get('Beruf', ''),
        image_generator_description=npc.attributes[config.VISUAL_APPEARANCE_ATTRIBUTE]
    )
