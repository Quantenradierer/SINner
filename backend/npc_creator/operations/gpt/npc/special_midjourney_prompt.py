import random

from npc_creator.repositories import template_image_repo


def transform_metatyp(metatyp):
    transformations = {
        "mensch": "human",
        "zwerg": "dwarf",
        "troll": "troll",
        "ork": "orc",
        "elf": "elf",
    }

    metatyp = metatyp.strip().lower()

    for key, intern in transformations.items():
        if key in metatyp:
            return intern

    return metatyp


def transform_gender(gender):
    gender = gender.lower()
    if gender == "männlich":
        return "male"
    elif gender == "weiblich":
        return "female"
    return ""


def get_multiprompts(metatyp_gender):
    return {
        "troll_male": "clothes:: small horns:: troll:: cyberpunk:: cyberpunkbackground::",
        "troll_female": "female::2 clothes:: small horns:: troll:: cyberpunk:: cyberpunkbackground:: ",
        "orc_male": "shadowrun:: modern orc::",
        "orc_female": "shadowrun:: modern orc::",
        "dwarf_male": "cyberpunk::0.5 dwarf:: gnome::-0.2 elf::-0.2",
        "dwarf_female": "cyberpunk::0.5 dwarf:: female:: gnome::-0.2 elf::-0.2",
    }.get(metatyp_gender, "cyberpunk::0.5")


def get_suffix_options(metatyp_gender):
    return {
        "troll_male": "--chaos "
        + str(random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)),
        "troll_female": "--chaos "
        + str(random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)),
    }.get(
        metatyp_gender,
        "--chaos "
        + str(random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)),
    ) + " --ar 4:5"


def special_midjourney_prompt(prompt, seed, metatyp, gender):
    prompt = prompt.strip()
    if not prompt.endswith("::"):
        prompt += "::"

    metatyp = transform_metatyp(metatyp)
    gender = transform_gender(gender)
    template = template_image_repo.find(f"{metatyp}_{gender}")
    if template:
        template_url = template.url
    else:
        template_url = ""
    multiprompts = get_multiprompts(f"{metatyp}_{gender}")
    suffix_options = get_suffix_options(f"{metatyp}_{gender}")

    seed_suffix = f"--seed {seed}"

    prompt = f"{template_url} {prompt} {multiprompts} {suffix_options} {seed_suffix}"
    return template, prompt
