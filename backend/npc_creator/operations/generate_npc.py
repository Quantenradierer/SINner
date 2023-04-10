from npc_creator import config
from npc_creator.config import GPT_CREATE_NPC_SYSTEM_PROMPT
from npc_creator.jobs import download_image
from npc_creator.models.npc import Npc
from npc_creator.operations.return_types import Failure, Success
from npc_creator.repositories import npc_repo
from npc_creator.services.gpt_prompts import create_npc_prompt, translate_appearance_prompt
from npc_creator.services.interpret_gpt import dict_from_text

from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated


class GenerateNpc:
    def __init__(self, user_prompt: str='', npc: Npc=None):
        self.user_prompt = user_prompt
        self.npc = npc

    def call(self):
        """
        Generates a random NPC based on a user-provided prompt.

        :returns: A new Npc object containing the attributes of the generated NPC.
        :rtype: Npc object
        """

        if self.npc:
            npc = self.npc
        else:
            npc = Npc()
            npc.user_prompt = self.user_prompt

        npc_prompt = create_npc_prompt(user_prompt=self.user_prompt,
                                       npc_attributes=npc.attributes,
                                       relevant_attributes=config.RELEVANT_ATTRIBUTES)
        gpt_completion = ask_chatgpt_moderated(GPT_CREATE_NPC_SYSTEM_PROMPT, npc_prompt)

        if not gpt_completion:
            return gpt_completion
        attributes = dict_from_text(config.RELEVANT_ATTRIBUTES, gpt_completion.data)
        if len(attributes) < len(config.RELEVANT_ATTRIBUTES) - 2:
            return Failure('gpt_result_insufficient')

        npc.add_attributes(attributes)
        npc_repo.create(npc)

        download_image.download_image_job_async(npc)

        return Success(data=npc)
