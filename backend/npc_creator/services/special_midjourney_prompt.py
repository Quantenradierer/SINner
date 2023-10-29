import random

from npc_creator.repositories import template_image_repo


def transform_metatyp(metatyp):
    transformations = {
        'mensch': 'human',
        'zwerg': 'dwarf',
        'troll': 'troll',
        'ork': 'orc',
        'elf': 'elf'
    }

    metatyp = metatyp.strip().lower()

    for key, intern in transformations.items():
        if key in metatyp:
            return intern

    return metatyp


def transform_gender(gender):
    gender = gender.lower()
    if gender == 'männlich':
        return 'male'
    elif gender == 'weiblich':
        return 'female'
    return ''


def get_multiprompts(metatyp_gender):
    return {
        'troll_male': 'small horns:: minotaur::0.8 clothes:: cyberpunk:: bull::-0.1 animal::-0.1 ',
        'troll_female': 'female::2 suit:: minotaur::1.5 small horns:: wrinkles:: clothes:: cyberpunk:: fur::-0.5 beard::-0.5 cyberpunk::',
        'orc_male': 'green skin::-0.3 wears jacket, suit or hoodie:: human with orc tusks:: armor::-0.1 ',
        'orc_female': 'green skin::-0.3 wears jacket, suit or hoodie:: human with orc tusks:: armor::-0.1 ',
        'dwarf_male': 'dwarf:: gnome::-0.2 elf::-0.2',
        'dwarf_female': 'dwarf:: gnome::-0.2 elf::-0.2'
    }.get(metatyp_gender, '')


def get_suffix_options(metatyp_gender):
    return {
        'troll_male': '--chaos ' + str(random.randint(1, 6) * random.randint(1, 6) + random.randint(1, 6)),
        'troll_female': '--chaos ' + str(random.randint(1, 6) * random.randint(1, 6) + random.randint(1, 6))
    }.get(metatyp_gender, '--chaos ' + str(random.randint(1, 6) * random.randint(1, 6) + 11 ))


def special_midjourney_prompt(prompt, seed, metatyp, gender):
    metatyp = transform_metatyp(metatyp)
    gender = transform_gender(gender)
    template = template_image_repo.find(f'{metatyp}_{gender}')
    if template:
        template_url = template.url
    else:
        template_url = ''

    multiprompts = get_multiprompts(f'{metatyp}_{gender}')
    suffix_options = get_suffix_options(f'{metatyp}_{gender}')

    seed_suffix = f'--seed {seed}'

    prompt = f'{template_url} {prompt}:: {multiprompts} {suffix_options} {seed_suffix}'
    return template, prompt
