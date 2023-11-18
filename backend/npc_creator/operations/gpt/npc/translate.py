from npc_creator.operations.gpt.gpt_interface import GptInterface
from .. import entity


class Translate(entity.Translate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """
- Übersetze ins Englische
- Übersetze in die Geschlechtsform entsprechend des Geschlechts welches am Anfang steht
- Forme die Sätze entsprechend um, das der Midjourney Bildgenerator bessere Bilder erzeugt
- Antworte nur mit der Übersetzung
"""

    def prompt(self):
        npc = self.kwargs["entity"]
        input_prompt = "Geschlecht: {gender}. Ein {alter} Jähriger mit Ethnizität {ethni}. Ein {metatyp} der als {beruf} tätig ist. {image_generator_description}"

        return [
            input_prompt.format(
                gender=npc.primary_values.get("Geschlecht", ""),
                metatyp=npc.primary_values.get("Metatyp", ""),
                beruf=npc.primary_values.get("Beruf", ""),
                alter=npc.primary_values.get("Alter", ""),
                ethni=npc.primary_values.get("Ethnizität"),
                image_generator_description=npc.primary_values[
                    "Detailliertes Aussehen"
                ],
            ),
        ]