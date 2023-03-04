import random
import time

import config
from factories.fill_npc_from_gpt import fill_npc_from_gpt
from models.npc import Npc
from repositories.npc import NpcRepository
from services.create_prompt import create_prompt
from services.gpt import Gpt


def generate_npc():
    """
    Generates one random NPC, without the image. Since the image may take longer, it will be generated separately
    """

    gpt = Gpt()
    npc_repo = NpcRepository()

    npc = Npc()
    prompt = create_prompt(npc=npc, attributes=config.RELEVANT_ATTRIBUTES)

    gpt_answer = gpt.ask_chatgpt(prompt)

    fill_npc_from_gpt(npc, gpt_answer)
    npc_repo.create(npc)
    return npc

if __name__ == '__main__':
    generate_npc()