import random
from copy import copy

from npc_creator import config

from typing import Any, Dict, List, Tuple


def create_npc_prompt(user_prompt: str, npc_attributes: Dict[str, str], relevant_attributes: List[str]) -> List:
    """
    Function to create a prompt for a non-player character (NPC) using the given attributes.
    The result will be in three parts: the user prompt itself, the current attributes and the missing attributes

    Parameters
    ----------
    user_prompt : str
        The user prompt text.
    npc_attributes : Dict[str, str]
        A dictionary containing the NPC's attributes.
    relevant_attributes : List[str]
        A list containing the all attributes to be considered.

    Returns
    -------
    List
        A list containing the user prompt, npc attributes, and other attributes.

    Examples
    --------
    >>> create_npc_prompt("Create a NPC", {"name": "John", "age": "30"}, ["name", "job", "age", "height"])
    ["Create a NPC", {"name": "John", "age": "30"}, {"job": "", "height": ""}]
    """

    npc_attributes_filtered = dict([(key, value) for key, value in npc_attributes.items() if value])
    attributes_filtered = dict([(key, "") for key in relevant_attributes if key not in npc_attributes_filtered])

    prompt_parts = [user_prompt, npc_attributes_filtered, attributes_filtered]

    formatted_prompts = []
    for prompt in prompt_parts:
        if type(prompt) is not str:
            prompt = '\n'.join([f'{key}: {value}' for key, value in prompt.items()])
        formatted_prompts.append(prompt)
    return formatted_prompts


def translate_appearance_prompt(npc):
    return config.TRANSLATE_INPUT_PROMPT.format(
        gender=npc.attributes.get('Geschlecht', ''),
        metatyp=npc.attributes.get('Metatyp', ''),
        beruf=npc.attributes.get('Beruf', ''),
        alter=npc.attributes.get('Alter', ''),
        ethni=npc.attributes.get('Ethnizität'),
        image_generator_description=npc.attributes[config.VISUAL_APPEARANCE_ATTRIBUTE]
    )
