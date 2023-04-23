from npc_creator import config
from npc_creator.config import MIDJOURNEY_PROMPT
from npc_creator.models.npc import Npc
from npc_creator.operations.return_types import Failure, Success
from npc_creator.repositories import npc_repo
from npc_creator.services.banned_words_filter import remove_banned_words
from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt
from npc_creator.services.gpt_prompts import translate_appearance_prompt
from npc_creator.services.midjourney.pass_prompt import pass_prompt
from npc_creator.services.special_midjourney_prompt import special_midjourney_prompt


class PassImagePrompt:
    def __init__(self, npc: Npc):
        """
        Constructor of the GenerateImage class.
        """
        self.npc = npc

    def call(self) -> Failure:
        """
        Generates the image for the NPC

        Returns:
            bool: True if the image creation was started, False otherwise.
        """

        if not self.npc.image_generator_description:
            translation_prompt = translate_appearance_prompt(self.npc)
            image_generator_description = ask_chatgpt(config.TRANSLATE_SYSTEM_PROMPT, [translation_prompt])
            if not image_generator_description:
                return Failure('gpt not available')

            self.npc.image_generator_description = remove_banned_words(image_generator_description.strip())
            npc_repo.save(self.npc)

        prompt = MIDJOURNEY_PROMPT.format(image_generator_description=self.npc.image_generator_description)
        prompt = special_midjourney_prompt(prompt,
                                           metatyp=self.npc.attributes.get('Metatyp', ''),
                                           gender=self.npc.attributes.get('Geschlecht', ''))
        prompt += ' ' + config.ADDITIONAL_PROMPT_OPTIONS

        if not pass_prompt(prompt):
            return Failure('sending_midjourney_prompt_was_unsuccessful')
        else:
            self.npc.image_generation_started()
            result = Success()

        npc_repo.save(self.npc)
        return result
