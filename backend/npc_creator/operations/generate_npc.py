from npc_creator import config
from npc_creator.jobs import download_image
from npc_creator.models.npc import Npc
from npc_creator.operations.return_types import Failure, Success
from npc_creator.repositories import npc_repo
from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt
from npc_creator.services.gpt_prompts import create_npc_prompt, translate_appearance_prompt
from npc_creator.services.interpret_gpt import dict_from_text


class GenerateNpc:
    def __init__(self, user_prompt: str):
        self.user_prompt = user_prompt

    def call(self):
        """
        Generates a random NPC based on a user-provided prompt.

        :returns: A new Npc object containing the attributes of the generated NPC.
        :rtype: Npc object
        """

        npc = Npc()

        npc.user_prompt = self.user_prompt

        npc_prompt = create_npc_prompt(user_prompt=self.user_prompt,
                                       npc_attributes=npc.attributes,
                                       attributes=config.RELEVANT_ATTRIBUTES)
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

        download_image.download_image_job_async(npc)

        return Success(data=npc)
