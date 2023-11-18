from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.services.banned_words_filter import remove_banned_words


class Translate(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = ""

    def prompt(self):
        raise NotImplementedError()

    def interpret_result(self, success):
        self.kwargs["entity"].image_generator_description = remove_banned_words(
            success.data.strip()
        )
        return success

    def handle_failure(self, failure):
        return failure
