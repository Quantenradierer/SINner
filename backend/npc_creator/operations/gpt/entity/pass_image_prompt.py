from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.return_types import Failure, Success
from npc_creator.services.image_generation.factory import ImageGeneratorFactory
from npc_creator.services.image_generation.store_image import store_entity_image


class PassImagePrompt:
    # Default prompt format - can be overridden by subclasses
    IMAGE_PROMPT_FORMAT = "In Shadowrun/Cyberpunk: {image_generator_description}"
    
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
        Generates the image for the entity using selected backend.
        
        Returns:
            bool: True if the image creation was started, False otherwise.
        """
        if not self.generation.description:
            result = self.generate_entity_image_description()
            self.generation.description = (
                result.data if result else self.entity.image_generator_description
            )

        prompt = self.IMAGE_PROMPT_FORMAT.format(
            image_generator_description=self.generation.description
        )
        
        # Get selected generator from factory
        generator = ImageGeneratorFactory.create_generator()
        
        # If we have a specific generator, use it; otherwise fallback to legacy Midjourney behavior
        if generator is not None:
            # New backends return the finished image directly (no Discord
            # round-trip, no Midjourney-style 4-up grid to split), so save
            # it and mark the generation done right away.
            image_bytes = generator.generate_image(prompt)
            if not image_bytes:
                return Failure("image_generation_failed")

            store_entity_image(image_bytes, self.entity, self.generation)

            self.generation.state = ImageGeneration.State.DONE
            self.generation.save()

            return Success()
        else:
            # Fallback to original Midjourney behavior for backward compatibility
            template, prompt = self.special_midjourney_prompt(prompt=prompt)
            
            from npc_creator.services.image_generation.pass_prompt import pass_prompt
            if not pass_prompt(prompt):
                return Failure("sending_midjourney_prompt_was_unsuccessful")
    
            self.generation.template = template
            self.generation.state = ImageGeneration.State.IN_PROGRESS
            self.generation.save()
    
            result = Success()
            return result

    def special_midjourney_prompt(self, prompt):
        """To be implemented by subclasses for Midjourney-specific prompts."""
        raise NotImplementedError("Subclasses must implement special_midjourney_prompt")