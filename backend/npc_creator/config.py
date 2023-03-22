import logging
import os

import openai


logging.basicConfig(filename='sinner.log')
logging.getLogger().setLevel(logging.DEBUG)

"""
file for the database
"""
SQLITE_FILE = 'data/npcs.sqlite'

"""
directory for npc images
"""
PUBLIC_NPC_IMAGE_PATH = os.getenv('PUBLIC_NPC_IMAGE_PATH') or 'frontend/public/images/npcs'

"""
file for 
"""
BANNED_WORD_FILE = 'data/midjourney_banned_words.txt'


"""
The images from midjourney will be saved temporary in this directory
"""
MIDJOURNEY_TEMP_PATH = 'data/midjourney'

"""
the prompt for midjourney
"""
MIDJOURNEY_PROMPT = 'In Shadowrun/Cyberpunk: {image_generator_description} --chaos 30 --ar 4:5'

"""
how often it shall be tried. The time between every try it calculated with '40 + pow(4, i)'
Means the waiting time is: 41s, 56s, 104s, ~5min, ~17min, ~68min.
After all this time the image generation counts as 'failed'.
This often happens when the image generation contains bad words, where the image couldn't get generated
"""
MIDJOURNEY_RETRIES_BEFORE_FAILING = 6

# noinspection PyPep8
"""
Prompt which will be sent to GPT. From my experience,
it is better to ask for the relevant points first and then give additional informations, cause otherwise it tries to create additional missing attributes or just answers directly without the attribute name
"""
PROMPT = "Vervollständige einen Shadowrun NPC. {user_prompt}.\n" \
         "Die folgenden Punkte müssen ergänzt werden. Sei beim Namen kreativ. Antworte nur auf Deutsch.\n" \
         "{missing_attributes}\n" \
         "-----\n" \
         "Hintergrundinformationen zu dem Charaktere.\n" \
         "{existing_attributes}\n"

"""
The translated result will be what midjourney gets. So this decides the midjourney results
"""
TRANSLATE_PROMPT = "Übersetzte den folgenden Abschnitt ins Englische: \nEin {alter} Jähriger {metatyp} der als {beruf} tätig ist. {image_generator_description}"

"""
the attribute which is used for visual appearance
"""
VISUAL_APPEARANCE_ATTRIBUTE = 'Detailliertes Aussehen'

"""
All relevant attributes, with default value. The default value can be overwritten by existing values of a npc.
"""
RELEVANT_ATTRIBUTES = {
    'Name': '',
    'Metatyp': '',
    'Beruf': '',
    'Ethnizität': '',
    'Geschlecht': '',
    'Alter': '',
    'Catchphrase': '',
    'Detailliertes Aussehen': '',
    'Hintergrundgeschichte': '',
    'Erfahrungen': '',
    'Ressentiments': '',
    'Motivationen': '',
    'Ziele': '',
    'Stärken': '',
    'Schwächen': '',
    'Fertigkeiten': '',
    'Ausrüstung': '',
    'Hobbys und Interessen': '',
    'Eigenarten': '',
    'Familie': '',
    'Kontakte': '',
    'Wohnort': '',
    'Nationalität': '',
    'Konzernzugehörigkeit': '',
    'Lootbare Gegenstände': '',
    'Geheimnis': '',
    'Konstitution (von 1-6)': '',
    'Geschicklichkeit (von 1-6)': '',
    'Reaktion (von 1-6)': '',
    'Stärke (von 1-6)': '',
    'Willenskraft (von 1-6)': '',
    'Logik (von 1-6)': '',
    'Intuition (von 1-6)': '',
    'Charisma (von 1-6)': '',
    'Glück (von 1-6)': '',
    'Magie (von 0-6)': '',
    'Resonanz (von 0-6)': ''
}

"""
configuration for openai
"""
openai.api_key = os.getenv('OPENAI_API_KEY')
