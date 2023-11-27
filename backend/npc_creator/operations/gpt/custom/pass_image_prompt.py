from npc_creator.operations.gpt import entity


def special_midjourney_prompt(prompt, parameters, seed):
    prompt = prompt.strip()
    if not prompt.endswith("::"):
        prompt += "::"

    seed_suffix = f"--seed {seed}"

    prompt = f"{prompt} {parameters} {seed_suffix}"
    return prompt


class PassImagePrompt(entity.PassImagePrompt):
    MIDJOURNEY_PROMPT = "{image_generator_description}"

    def special_midjourney_prompt(self, prompt):
        parameters = self.entity.primary_values.get("Parameter", "")
        return None, (
            special_midjourney_prompt(prompt, parameters, seed=self.generation.id)
        )
