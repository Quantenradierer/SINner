from npc_creator import config
from npc_creator.config import MIDJOURNEY_PROMPT
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.gpt.translate_description import TranslateDescription
from npc_creator.operations.return_types import Failure, Success
from npc_creator.services.midjourney.pass_prompt import pass_prompt
from npc_creator.services.special_midjourney_prompt import special_midjourney_prompt


class PassImagePrompt:
    def __init__(self, generation: ImageGeneration):
        self.generation = generation
        self.npc = self.generation.entity

    def generate_npc_image_description(self):
        result = TranslateDescription(npc=self.npc).call()
        if result:
            self.npc.save()
        return result

    def call(self) -> Failure:
        """
        Generates the image for the NPC

        Returns:
            bool: True if the image creation was started, False otherwise.
        """
        if not self.generation.description:
            self.generate_npc_image_description()
            self.generation.description = self.npc.image_generator_description

        prompt = MIDJOURNEY_PROMPT.format(
            image_generator_description=self.generation.description
        )
        template, prompt = special_midjourney_prompt(
            prompt,
            seed=self.generation.id,
            metatyp=self.npc.primary_values.get("Metatyp", ""),
            gender=self.npc.primary_values.get("Geschlecht", ""),
        )
        prompt += " " + config.ADDITIONAL_PROMPT_OPTIONS

        if not pass_prompt(prompt):
            return Failure("sending_midjourney_prompt_was_unsuccessful")

        self.generation.template = template
        self.generation.state = ImageGeneration.State.IN_PROGRESS
        self.generation.save()

        result = Success()
        return result
