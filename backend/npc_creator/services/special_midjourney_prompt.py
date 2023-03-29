from npc_creator.repositories import template_image


def transform_metatyp(metatyp):
    transformations = {
        'mensch': 'human',
        'zwerg': 'dwarf',
        'troll': 'troll',
        'ork': 'orc',
        'elf': 'elf'
    }

    metatyp = metatyp.lower()

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
        'troll_male': 'small horns:: minotaur::0.8 bull::-0.1 animal::-0.1 ',
        'troll_female': 'female::3 suit:: minotaur::0.8 small horns:: wrinkles:: fur::-0.5 beard::-0.5 cyberpunk::',
        'orc_male': 'orc::',
        'orc_female': 'orc::',
        'dwarf_male': 'dwarf::',
        'dwarf_female': 'dwarf::'
    }.get(metatyp_gender, '')


def get_suffix_options(metatyp_gender):
    return {
        'troll_male': '--chaos 8 --v 5',
        'troll_female': '--chaos 8 --v 5'
    }.get(metatyp_gender, '--chaos 30')


def special_midjourney_prompt(prompt, metatyp, gender):
    metatyp = transform_metatyp(metatyp)
    gender = transform_gender(gender)

    template_url = template_image.find(f'{metatyp}_{gender}')
    if template_url:
        template_url = template_url.url
    else:
        template_url = ''

    multiprompts = get_multiprompts(f'{metatyp}_{gender}')
    suffix_options = get_suffix_options(f'{metatyp}_{gender}')

    prompt = f'{template_url} {prompt}:: {multiprompts} {suffix_options}'
    return prompt
