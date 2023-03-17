import config
from models.npc import Npc
from operations.operation_output import Failure, Success
from operations.pass_image_prompt import PassImagePrompt
from operations import download_image
from repositories.npc import NpcRepository
from services.gpt.ask_chatgpt import ask_chatgpt
from services.gpt_prompts import create_npc_prompt, translate_appearance_prompt
from services.interpret_gpt import dict_from_text


class GenerateNpc:
    def __init__(self, user_prompt:str):
        self.user_prompt = user_prompt

    def call(self):
        """
        Generates a random NPC based on a user-provided prompt.

        :param user_prompt: The prompt provided by the user.
        :type user_prompt: str

        :returns: A new Npc object containing the attributes of the generated NPC.
        :rtype: Npc object
        """

        npc = Npc()

        npc_repo = NpcRepository()
        npc.user_prompt = self.user_prompt

        npc_prompt = create_npc_prompt(self.user_prompt, npc=npc, attributes=config.RELEVANT_ATTRIBUTES)
        gpt_completion = ask_chatgpt(npc_prompt)
        if not gpt_completion:
            return Failure('gpt not available')
        npc.add_attributes(dict_from_text(config.RELEVANT_ATTRIBUTES.keys(), gpt_completion))

        translation_prompt = translate_appearance_prompt(npc)
        image_generator_description = ask_chatgpt(translation_prompt)
        if not npc_prompt:
            return Failure('gpt not available')

        npc.image_generator_description = image_generator_description.strip()
        npc_repo.create(npc)

        PassImagePrompt(npc).call()
        npc_repo.save(npc)

        download_image.download_image_job_async(npc)

        return Success(data=npc)
