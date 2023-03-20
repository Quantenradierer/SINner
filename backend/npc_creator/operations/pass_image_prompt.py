from npc_creator.config import MIDJOURNEY_PROMPT
from npc_creator.models.npc import Npc
from npc_creator.operations.return_types import Failure, Success
from npc_creator.repositories import npc_repo
from npc_creator.services.banned_words_filter import contains_banned_word
from npc_creator.services.midjourney.pass_prompt import pass_prompt


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
        if not self.npc.requires_image_generation():
            return Failure('image generation for this npc already started')
        if contains_banned_word(self.npc.image_generator_description):
            self.npc.image_generation_used_banned_word()
            result = Failure('contains banned word')
        elif not pass_prompt(MIDJOURNEY_PROMPT.format(image_generator_description=self.npc.image_generator_description)):
            return Failure('sending midjourney prompt was unsuccessful')
        else:
            self.npc.image_generation_started()
            result = Success()

        npc_repo.save(self.npc)
        return result
