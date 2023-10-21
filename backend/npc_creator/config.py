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
Prompt which will be sent to GPT. From my experience,
it is better to ask for the relevant points first and then give additional informations, cause otherwise it tries to create additional missing attributes or just answers directly without the attribute name
"""


GPT_CREATE_NPC_SYSTEM_PROMPT = """- Vervollständige einen NPC für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Erstelle unangemessene, extreme, rassistische oder homophobe NPC so, das du zeigst wie falsch ihre Werte sind 
- Erstelle keine Urheberrechtlich geschützten Figuren oder Personen
- Erstelle keine Runner oder Söldner, sofern nicht anders gewünscht
- Das Geheimnis muss detailliert beschrieben sein
- Der Name ist in der Form 'Vorname "Rufname" Nachname' 
- Sei beim Namen kreativ
- Nutze seltene und unübliche Namen 
- Achte darauf, den NPC in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
- Beachte die geänderte Weltordnung, Länder und Regionen der Sechsten Welt von Shadowrun 
- Zwerge sind keine Schmiede oder Braumeister, sondern gehen reguläre Berufe der Modernen Zeit nach
"""


"""
The translated result will be what midjourney gets. So this decides the midjourney results
"""
TRANSLATE_SYSTEM_PROMPT = """- Übersetze ins Englische
- Antworte nur mit der Übersetzung
"""

TRANSLATE_INPUT_PROMPT = "Ein {alter} Jähriger mit Ethnizität {ethni}. Ein {metatyp} der als {beruf} tätig ist. {image_generator_description}"

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

