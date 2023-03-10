from backend import config
from repositories.npc import NpcRepository
from services.gpt import Gpt
from services.gpt_prompts import create_npc_prompt
from services.interpret_gpt import dict_from_text


def regenerate_npc(id: int):
    """
    To be used when the configuration changes.
    Generates all attributes which are not set. Removes all attributes which are not in the configuration listed.
    The existing attributes will be given to GPT, so the result will be somehow similar
    :param id: NPC id
    """
    gpt = Gpt()
    npc_repo = NpcRepository()

    npc = npc_repo.find(id)

    npc_prompt = create_npc_prompt(user_prompt=npc.user_prompt, npc=npc, attributes=config.RELEVANT_ATTRIBUTES)
    if npc_prompt is None:
        return npc

    gpt_completion = gpt.ask_chatgpt(npc_prompt)
    npc.add_attributes(dict_from_text(config.RELEVANT_ATTRIBUTES.keys(), gpt_completion))

    npc_repo.create(npc)
    return npc
