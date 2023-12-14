import random


def get_multiprompts():
    return "cyberpunk::0.3"


def get_suffix_options():
    return (
        "--chaos " + str(random.randint(1, 2) * random.randint(1, 3) + 5) + " --ar 7:4"
    )


def special_midjourney_prompt(prompt, seed):
    prompt = prompt.strip()
    if not prompt.endswith("::"):
        prompt += "::"

    multiprompts = get_multiprompts()
    suffix_options = get_suffix_options()
    seed_suffix = f"--seed {seed}"

    prompt = f"{prompt} {multiprompts} {suffix_options} {seed_suffix}"
    return None, prompt
