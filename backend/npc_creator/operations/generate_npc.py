from pymonad.either import Either, Left, Right

from npc_creator import config
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.npc import Npc
from npc_creator.operations.gpt.fill_npc import FillNpc
from npc_creator.operations.return_types import Failure, Success
from npc_creator.services.interpret_gpt import dict_from_text

from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated


class GenerateNpc:
    def __init__(self, user_prompt: str='', npc: Npc=None):
        self.npc = npc or Npc()
        self.user_prompt = user_prompt

    def call(self):
        result = FillNpc(npc=self.npc, user_prompt=self.user_prompt).call()
        if result:
            return Success(data=self.npc)
        return Failure(error=result.error)
