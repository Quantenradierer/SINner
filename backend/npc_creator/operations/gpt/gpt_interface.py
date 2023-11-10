from enum import Enum

from npc_creator.models.gpt_request import GptRequest
from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated


class GptInterface:
    class GptVersion(Enum):
        GPT3_5 = "gpt-3.5-turbo"
        GPT4 = "gpt-4"
        GPT4_TURBO = "gpt-4-1106-preview"

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.request = GptRequest(kind=str(self.__class__.__name__))
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = ""

    def prompt(self):
        raise NotImplementedError()

    def interpret_result(self, success):
        raise success

    def handle_failure(self, failure):
        return failure

    def call(self):
        self.request.input = self.prompt()

        output = ask_chatgpt_moderated(
            self.system_prompt, self.request.input, gpt=self.gpt.value
        )
        self.request.output = str(output.data)
        if not output:
            self.request.failed()
            self.request.save()
            return self.handle_failure(output)

        self.request.finished()
        self.request.save()
        return self.interpret_result(output)
