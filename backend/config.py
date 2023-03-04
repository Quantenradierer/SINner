

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

SQLITE_FILE = 'data/npcs.sqlite'


"""
Prompt which will be sent to GPT, followed by a list of the attributes
"""
PROMPT = "Vervollständige einen Shadowrun NPC mit Bezug auf die ADL, Allianz Deutscher Länder, mit den folgenden Attributen. Antworte dazu mit allen genannten Punkten, inklusive der Werte, erneut: \n"


"""
All relevant attributes, with default value. The main keys (Aussehen, Hintergrund, etc) do not have a function at the moment.
The default value can be overwritten by existing values of a npc.
"""
RELEVANT_ATTRIBUTES = {
    'Aussehen': {
        'Name': '',
        'Metatype': '',
        'Beruf': '',
        'Ethnizität': '',
        'Geschlecht': '',
        'Alter': '',
        'Geruch': '',
        'Catchphrase': '',
        'Detailliertes Aussehen': '',
        'Detailliertes Aussehen (english)': ''
    },
    'Hintergrund': {
        'Hintergrundgeschichte': '',
        'Erfahrungen': '',
        'Ressentiments': '',
        'Motivationen': '',
        'Ziele': '',
        'Stärken': '',
        'Schwächen': ''
    },
    'Fertigkeiten': {
        'Fertigkeiten': '',
        'Ausrüstung': '',
        'Ruf': '',
        'Geld': '',
        'Ressourcen': ''
    },
    #'Attribute': ['Stärke (von 1-6)', 'Konstitution (von 1-6)', 'Intuition (von 1-6)', 'Reaktion (von 1-6)', 'Geschicklichkeit (von 1-6)', 'Willenskraft (von 1-6)', 'Glück (von 1-6)', 'Magie (von 0-6)', 'Resonanz (von 0-6)']
    'Privat': {
        'Hobbys und Interessen': '',
        'Eigenarten': '',
        'Familienstand': '',
        'Familie': '',
        'Kinder': '',
        'Kontakte': '',
        'Wohnort': '',
        'Nationalität': '',
        'Konzernzugehörigkeit': ''
    }
}


'''
midjourney adds the username in front of the image name. We need the name in order to remove it.
'''
MIDJOURNEY_USERNAME = 'Leto'