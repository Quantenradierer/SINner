from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt import entity


class Translate(entity.Translate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """
- you are a professional illustrator with 100 years of experience
- if you do a good job, you will receive 1000€ tip
- generate a midjourney prompt for image generation
- do not use parameters
- answer only in english, no matter the input language
- add humans or even crowd of humans into the refined prompt if they fit into the scene
- answer only with the refined version
"""

    #    - end the refined version with :: then add the type of location at end again ending with ::

    def prompt(self):
        entity = self.kwargs["entity"]
        input_prompt = "{image_generator_description}"

        return [
            input_prompt.format(
                image_generator_description=entity.primary_values["Aussehen"]
            ),
        ]
