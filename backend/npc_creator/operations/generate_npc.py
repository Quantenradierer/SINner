from pymonad.either import Either, Left, Right

from npc_creator import config
from npc_creator.config import GPT_CREATE_NPC_SYSTEM_PROMPT
from npc_creator.jobs import download_image
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.npc import Npc
from npc_creator.operations.recreate_image import RecreateImage
from npc_creator.operations.return_types import Failure, Success
from npc_creator.repositories import npc_repo
from npc_creator.services.gpt_prompts import create_npc_prompt, translate_appearance_prompt
from npc_creator.services.interpret_gpt import dict_from_text

from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated


class GenerateNpc:
    def __init__(self, user_prompt: str='', npc: Npc=None):
        self.npc = npc or Npc(user_prompt=user_prompt)
        self.user_prompt = user_prompt

    def format_npc(self):
        npc_prompt = create_npc_prompt(user_prompt=self.user_prompt,
                                       npc_attributes=self.npc.attributes,
                                       relevant_attributes=config.RELEVANT_ATTRIBUTES)
        gpt_request = GptRequest(input=npc_prompt)
        return gpt_request

    def update_npc_with_gpt_data(self, gpt_request):
        gpt_request = self.format_npc()

        gpt_completion = ask_chatgpt_moderated(config.GPT_CREATE_NPC_SYSTEM_PROMPT, gpt_request.input)
        if gpt_completion:
            gpt_request.finished(gpt_completion.data)
            attributes = dict_from_text(config.RELEVANT_ATTRIBUTES, gpt_completion.data)
            self.npc.add_attributes(attributes)
        else:
            gpt_request.failed()
        gpt_request.save()
        return gpt_completion

    def is_attributes_sufficient(self):
        return len([value for value in self.npc.attributes.values() if value]) >= len(config.RELEVANT_ATTRIBUTES) - 2

    def save_and_visualize_npc(self):
        npc_repo.create(self.npc)
        RecreateImage(self.npc).call()

    def call(self):
        gpt_completion = self.update_npc_with_gpt_data(self.user_prompt)
        if not gpt_completion:
            return gpt_completion
        if not self.is_attributes_sufficient():
            return Failure('gpt_result_insufficient')
        self.save_and_visualize_npc()
        return Success(data=self.npc)
