import config
from models.npc import Npc
from operations.generage_image import generate_image_job_async
from repositories.npc import NpcRepository
from services.gpt import Gpt
from services.gpt_prompts import create_npc_prompt, translate_appearance_prompt
from services.interpret_gpt import dict_from_text


def generate_npc(user_prompt: str):
    """
    Generates a random NPC based on a user-provided prompt.

    :param user_prompt: The prompt provided by the user.
    :type user_prompt: str

    :returns: A new Npc object containing the attributes of the generated NPC.
    :rtype: Npc object
    """

    gpt = Gpt()
    npc_repo = NpcRepository()

    npc = Npc()
    npc.user_prompt = user_prompt

    npc_prompt = create_npc_prompt(user_prompt, npc=npc, attributes=config.RELEVANT_ATTRIBUTES)
    gpt_completion = gpt.ask_chatgpt(npc_prompt)
    npc.add_attributes(dict_from_text(config.RELEVANT_ATTRIBUTES.keys(), gpt_completion))

    translation_prompt = translate_appearance_prompt(npc)
    npc.image_generator_description = gpt.ask_chatgpt(translation_prompt).strip()

    npc_repo.create(npc)
    generate_image_job_async(npc)

    return npc


if __name__ == '__main__':
    for i in range(1):
        generate_npc('')
