from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.return_types import Failure, Success
from npc_creator.services.midjourney.pass_prompt import pass_prompt


class PassImagePrompt:
    MIDJOURNEY_PROMPT = "In Shadowrun/Cyberpunk: {image_generator_description}"

    def special_midjourney_prompt(self):
        raise NotImplementedError

    def __init__(self, generation: ImageGeneration):
        self.generation = generation
        self.entity = self.generation.entity

    def generate_entity_image_description(self):
        entity = self.entity.instance
        result = entity.Translate(entity=self.entity).call()

        if result:
            entity.image_generator_description = result.data
            entity.save()
        return result

    def call(self) -> Failure:
        """
        Generates the image for the NPC

        Returns:
            bool: True if the image creation was started, False otherwise.
        """
        if not self.generation.description:
            self.generate_entity_image_description()
            self.generation.description = self.entity.image_generator_description

        prompt = self.MIDJOURNEY_PROMPT.format(
            image_generator_description=self.generation.description
        )
        template, prompt = self.special_midjourney_prompt(prompt=prompt)

        if not pass_prompt(prompt):
            return Failure("sending_midjourney_prompt_was_unsuccessful")

        self.generation.template = template
        self.generation.state = ImageGeneration.State.IN_PROGRESS
        self.generation.save()

        result = Success()
        return result
