from npc_creator import config
from npc_creator.models import Entity


def entity_prompt(entity):
    """ """
    npc_attributes = entity.primary_values
    npc_attributes_filtered = dict(
        [(key, value) for key, value in npc_attributes.items() if value]
    )
    attributes_filtered = dict(
        [
            (attr_def.name, "")
            for attr_def in entity.ATTRIBUTE_DEFINITION
            if attr_def.name not in npc_attributes_filtered
        ]
    )

    prompt_parts = [npc_attributes_filtered, attributes_filtered]

    formatted_prompts = []
    for prompt in prompt_parts:
        if type(prompt) is not str:
            prompt = "\n".join([f"{key}: {value}" for key, value in prompt.items()])
        formatted_prompts.append(prompt)
    return formatted_prompts
