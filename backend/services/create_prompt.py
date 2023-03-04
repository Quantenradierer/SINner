from collections import ChainMap
from config import PROMPT


def create_prompt(npc, attributes):
    prompt = PROMPT

    flat_attributes = ChainMap(*attributes.values())

    for attribute in npc.attributes:
        flat_attributes[attribute.key] = attribute.value

    for item in flat_attributes.items():
        prompt += f'{item[0]}: {item[1]}\n'

    return prompt
