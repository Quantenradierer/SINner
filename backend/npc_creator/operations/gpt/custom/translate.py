from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt import entity


class Translate(entity.Translate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """
- you are a professional illustrator with 100 years of experience
- if you do a good job, you will receive 200€ tip
- generate a midjourney prompt for image generation
- do not use parameters
- do not use simple quotes 
- do not use double quotes, except for words which shall be visible in the image as text
- answer only in english, no matter the input language
- answer only with the refined version, no further text
"""

    def prompt(self):
        entity = self.kwargs["entity"]
        input_prompt = "{image_generator_description}"

        return [
            input_prompt.format(
                image_generator_description=entity.primary_values["Aussehen"]
            ),
        ]
