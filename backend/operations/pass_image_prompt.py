
from models.npc import Npc
from operations.operation_output import Failure, Success
from repositories.npc import NpcRepository
from config import MIDJOURNEY_PROMPT
from services.banned_words_filter import contains_banned_word
from services.midjourney.pass_prompt import pass_prompt


class PassImagePrompt:
    def __init__(self, npc: Npc):
        """
        Constructor of the GenerateImage class.

        Args:
            npc_id (int): The ID of the NPC for which the image should be generated.
        """
        self.repo = NpcRepository()
        self.npc = npc

    def call(self) -> bool:
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

        self.repo.save(self.npc)
        return result
