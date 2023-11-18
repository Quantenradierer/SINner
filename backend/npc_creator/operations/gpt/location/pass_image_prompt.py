from npc_creator.operations.gpt import entity
from .special_midjourney_prompt import special_midjourney_prompt


class PassImagePrompt(entity.PassImagePrompt):
    def special_midjourney_prompt(self, prompt):
        return special_midjourney_prompt(prompt, seed=self.generation.id)
