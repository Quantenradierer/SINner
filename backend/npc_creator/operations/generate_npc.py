from pymonad.either import Either, Left, Right

from npc_creator import config
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.npc import Npc
from npc_creator.operations.return_types import Failure, Success
from npc_creator.repositories import npc_repo
from npc_creator.services.gpt_prompts import create_npc_prompt, translate_appearance_prompt
from npc_creator.services.interpret_gpt import dict_from_text

from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated


class GenerateNpc:
    def __init__(self, user_prompt: str='', npc: Npc=None):
        self.npc = npc or Npc()
        self.user_prompt = user_prompt

    def format_npc(self):
        npc_prompt = create_npc_prompt(user_prompt=self.user_prompt,
                                       npc_attributes=self.npc.attributes,
                                       relevant_attributes=config.RELEVANT_ATTRIBUTES)
        gpt_request = GptRequest(input=npc_prompt)
        return gpt_request

    def get_empty_attribute(self):
        '''
        Returns: the empty attribute, if there is only one, or None otherwise
        '''
        for key, value in self.npc.attributes.items():
            if not value.strip():
                return key


    def update_npc_with_gpt_data(self, gpt_request):
        gpt_request = self.format_npc()

        gpt_completion = ask_chatgpt_moderated(config.GPT_CREATE_NPC_SYSTEM_PROMPT, gpt_request.input, gpt='gpt-3.5-turbo')
        if gpt_completion:
            gpt_request.finished(gpt_completion.data)
            attributes = dict_from_text(config.RELEVANT_ATTRIBUTES, gpt_completion.data)

            if not attributes:
                empty_attribute = self.get_empty_attribute()
                if empty_attribute:
                    attributes = {empty_attribute: gpt_completion.data}

            self.npc.add_attributes(attributes)
        else:
            gpt_request.failed()
        gpt_request.save()
        return gpt_completion

    def call(self):
        gpt_completion = self.update_npc_with_gpt_data(self.user_prompt)
        if not gpt_completion:
            return gpt_completion
        return Success(data=self.npc)
