from npc_creator import config


def npc_prompt(npc):
    """
    """
    npc_attributes = npc.attributes
    relevant_attributes = config.RELEVANT_ATTRIBUTES

    npc_attributes_filtered = dict([(key, value) for key, value in npc_attributes.items() if value])
    attributes_filtered = dict([(key, "") for key in relevant_attributes if key not in npc_attributes_filtered])

    prompt_parts = [npc_attributes_filtered, attributes_filtered]

    formatted_prompts = []
    for prompt in prompt_parts:
        if type(prompt) is not str:
            prompt = '\n'.join([f'{key}: {value}' for key, value in prompt.items()])
        formatted_prompts.append(prompt)
    return formatted_prompts