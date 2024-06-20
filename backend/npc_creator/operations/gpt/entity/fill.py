import json

from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.services.interpret_gpt import dict_from_text


class Fill(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = ""

    @property
    def entity(self):
        return self.kwargs["entity"]

    @property
    def user_prompt(self):
        return self.kwargs.get("user_prompt", "")

    def prompt(self):
        return [self.user_prompt] + entity_prompt(self.entity)

    def interpret_result(self, success):
        attributes = success.data
        self.entity.add_values(attributes)
        return success
