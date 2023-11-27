from npc_creator.operations.gpt import entity


def special_midjourney_prompt(prompt, seed):
    prompt = prompt.strip()
    if not prompt.endswith("::"):
        prompt += "::"

    seed_suffix = f"--seed {seed}"

    prompt = f"{prompt} {seed_suffix}"
    return None, prompt


class PassImagePrompt(entity.PassImagePrompt):
    MIDJOURNEY_PROMPT = "{image_generator_description}"

    def special_midjourney_prompt(self, prompt):
        return special_midjourney_prompt(prompt, seed=self.generation.id)
