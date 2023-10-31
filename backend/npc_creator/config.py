import logging
import os
import sys

import openai
import requests


logging.basicConfig(filename='schattenakte.log')
logging.getLogger().setLevel(logging.DEBUG)

"""
file for the database
"""
SQLITE_FILE = 'data/npcs.sqlite'

"""
directory for npc images
"""
PUBLIC_NPC_IMAGE_PATH = os.getenv('PUBLIC_NPC_IMAGE_PATH')

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
MIDJOURNEY_PROMPT = 'In Shadowrun/Cyberpunk: {image_generator_description}'
ADDITIONAL_PROMPT_OPTIONS = '--ar 4:5'

"""
how often it shall be tried. The time between every try it calculated with '40 + pow(3, i)'
Means the waiting time is: 31s, 46s, 94s, ~5min, ~17min, ~68min.
After all this time the image generation counts as 'failed'.
This often happens when the image generation contains bad words, where the image couldn't get generated
"""
MIDJOURNEY_RETRIES_BEFORE_FAILING = 8

# noinspection PyPep8
"""
The translated result will be what midjourney gets. So this decides the midjourney results
"""
TRANSLATE_SYSTEM_PROMPT = """- Übersetze ins Englische
- Antworte nur mit der Übersetzung
- Übersetze in die Geschlechtsform entsprechend des Geschlechts welches am Anfang steht
"""

TRANSLATE_INPUT_PROMPT = "Geschlecht: {gender}. Ein {alter} Jähriger mit Ethnizität {ethni}. Ein {metatyp} der als {beruf} tätig ist. {image_generator_description}"

"""
the attribute which is used for visual appearance
"""
VISUAL_APPEARANCE_ATTRIBUTE = 'Detailliertes Aussehen'

"""
All relevant attributes, with default value. The default value can be overwritten by existing values of a npc.
"""
RELEVANT_ATTRIBUTES = ['Beruf', 'Metatyp', 'Ethnizität', 'Geschlecht', 'Alter', 'Catchphrase', 'Detailliertes Aussehen', 'Name', 'Hintergrundgeschichte',  'Erfahrungen', 'Ressentiments', 'Motivationen', 'Ziele', 'Stärken', 'Schwächen', 'Fertigkeiten', 'Ausrüstung', 'Hobbys und Interessen', 'Eigenarten', 'Familie', 'Kontakte', 'Lootbare Gegenstände', 'Geheimnis', 'Konstitution (von 1-6)', 'Geschicklichkeit (von 1-6)', 'Reaktion (von 1-6)', 'Stärke (von 1-6)', 'Willenskraft (von 1-6)', 'Logik (von 1-6)', 'Intuition (von 1-6)', 'Charisma (von 1-6)', 'Glück (von 1-6)', 'Magie (von 0-6)', 'Resonanz (von 0-6)']


"""
configuration for openai
"""
openai.api_key = os.getenv('OPENAI_API_KEY')


if 'test' in sys.argv:
    def mock(*args, **kwargs):
        raise Exception('if this has raised in your test, your mocks do not work.')

    openai.create = mock
    requests.get = mock
    requests.post = mock

