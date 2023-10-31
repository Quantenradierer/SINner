from enum import Enum

from npc_creator.models.gpt_request import GptRequest
from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.services.banned_words_filter import remove_banned_words
from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated


class TranslateDescription(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4
        self.system_prompt = """- Übersetze ins Englische
- Antworte nur mit der Übersetzung
- Übersetze in die Geschlechtsform entsprechend des Geschlechts welches am Anfang steht
"""

    def prompt(self):
        npc = self.kwargs['npc']
        input_prompt = "Geschlecht: {gender}. Ein {alter} Jähriger mit Ethnizität {ethni}. Ein {metatyp} der als {beruf} tätig ist. {image_generator_description}"

        return [input_prompt.format(
            gender=npc.attributes.get('Geschlecht', ''),
            metatyp=npc.attributes.get('Metatyp', ''),
            beruf=npc.attributes.get('Beruf', ''),
            alter=npc.attributes.get('Alter', ''),
            ethni=npc.attributes.get('Ethnizität'),
            image_generator_description=npc.attributes['Detailliertes Aussehen']
        ),]

    def interpret_result(self, success):
        self.kwargs['npc'].image_generator_description = remove_banned_words(success.data.strip())
        return success

    def handle_failure(self, failure):
        return failure

"""
            translation_prompt = translate_appearance_prompt(self.npc)
            image_generator_description = ask_chatgpt_moderated(, [translation_prompt])
            if not image_generator_description:
                return image_generator_description

            
            """