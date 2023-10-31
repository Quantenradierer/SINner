from npc_creator import config


def translate_appearance_prompt(npc):
    return config.TRANSLATE_INPUT_PROMPT.format(
        gender=npc.attributes.get('Geschlecht', ''),
        metatyp=npc.attributes.get('Metatyp', ''),
        beruf=npc.attributes.get('Beruf', ''),
        alter=npc.attributes.get('Alter', ''),
        ethni=npc.attributes.get('Ethnizität'),
        image_generator_description=npc.attributes[config.VISUAL_APPEARANCE_ATTRIBUTE]
    )
