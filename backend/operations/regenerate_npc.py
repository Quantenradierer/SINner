import random
import time

import backend.config
from factories.fill_npc_from_gpt import fill_npc_from_gpt
from repositories.npc import NpcRepository
from services.create_prompt import create_prompt
from services.gpt import Gpt


def regenerate_npc(id):
    """
    To be used when the configuration changes.
    Generates all attributes which are not set. Removes all attributes which are not in the configuration listed.
    The existing attributes will be given to GPT, so the character will be somehow similar
    :param id: NPC id
    """
    gpt = Gpt()
    npc_repo = NpcRepository()

    npc = npc_repo.find(id)
    prompt = create_prompt(npc=npc, attributes=config.RELEVANT_ATTRIBUTES)

    gpt_answer = gpt.ask_chatgpt(prompt)

    fill_npc_from_gpt(npc, gpt_answer)
    npc_repo.create(npc)
    return npc


if __name__ == '__main__':
    regenerate_npc(3)