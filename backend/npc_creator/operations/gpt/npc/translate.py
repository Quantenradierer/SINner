from npc_creator.operations.gpt.gpt_interface import GptInterface
from .. import entity


class Translate(entity.Translate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = """
- if you do a good job, you will receive 200€ tip
- do not use quotes for names
- do not use simple quotes 
- do only use double quotes for words which shall be visible as text in the image itself
- generate a midjourney prompt for image generation
- do not use midjourney parameters
- answer only in english, no matter the input language
- answer only with the refined version, no further text
"""

    def prompt(self):
        npc = self.kwargs["entity"]
        input_prompt = "Geschlecht: {gender}. Ein {alter} Jähriger mit Ethnizität {ethni}. Ein {metatyp} der als {beruf} tätig ist. {image_generator_description}"

        return [
            input_prompt.format(
                gender=npc.attributes.get("gender", ""),
                metatyp=npc.attributes.get("metatype", ""),
                beruf=npc.attributes.get("profession", ""),
                alter=npc.attributes.get("age", ""),
                ethni=npc.attributes.get("ethnicity", ""),
                image_generator_description=npc.attributes["appearance"],
            ),
        ]
