import random

from npc_creator.repositories import template_image_repo


def get_multiprompts():
    return "cyberpunk::0.3"


def get_suffix_options():
    return (
        "--chaos " + str(random.randint(1, 6) * random.randint(1, 6) + 11) + " --ar 5:4"
    )


def special_midjourney_prompt(prompt, seed):
    multiprompts = get_multiprompts()
    suffix_options = get_suffix_options()
    seed_suffix = f"--seed {seed}"

    prompt = f"{prompt}:: {multiprompts} {suffix_options} {seed_suffix}"
    return None, prompt
