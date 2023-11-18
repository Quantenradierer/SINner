from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt import entity


class Translate(entity.Translate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """
- Übersetze ins Englische
- Forme die Sätze entsprechend um, das der Midjourney Bildgenerator bessere Bilder erzeugt
- Antworte nur mit der Übersetzung
"""

    def prompt(self):
        entity = self.kwargs["entity"]
        input_prompt = "{image_generator_description}"

        return [
            input_prompt.format(
                image_generator_description=entity.primary_values["Aussehen"]
            ),
        ]
