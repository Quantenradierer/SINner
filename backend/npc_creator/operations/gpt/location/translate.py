from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt import entity


class Translate(entity.Translate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """
- translate the prompt into english
- improve the given prompt for "Mid Journey"
- add humans or even crowd of humans into the refined prompt if they fit into the scene
- answer only with the refined version
- end the refined version with :: then add the type of location at end again ending with ::
- if it is a indoor location add the word 'ceiling' and end with :: again 
"""

    def prompt(self):
        entity = self.kwargs["entity"]
        input_prompt = "{image_generator_description}"

        return [
            input_prompt.format(
                image_generator_description=entity.primary_values["Aussehen"]
            ),
        ]
