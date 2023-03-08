

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

SQLITE_FILE = 'data/npcs.sqlite'


"""
Prompt which will be sent to GPT. From my experience,
it is better to ask for the relevant points first and then give additional informations, cause otherwise it tries to create additional missing attributes or just answers directly without the attribute name
"""
PROMPT = "Vervollständige einen Shadowrun NPC. {user_prompt}" \
         "Die folgenden Punkte müssen ergänzt werden. Antworte nur auf Deutsch.\n" \
         "{missing_attributes}\n" \
         "-----\n" \
         "Hintergrundinformationen zu dem Charaktere.\n" \
         "{existing_attributes}\n" \

TRANSLATE_PROMPT = "Übersetzte den folgenden Abschnitt ins Englische: \n{text}\n"

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
    'Geruch': '',
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
    'Ruf': '',
    'Geld': '',
    'Ressourcen': '',
    'Hobbys und Interessen': '',
    'Eigenarten': '',
    'Familienstand': '',
    'Familie': '',
    'Kinder': '',
    'Kontakte': '',
    'Wohnort': '',
    'Nationalität': '',
    'Konzernzugehörigkeit': '',
    'Lootbare Gegenstände': '',
    'Geheimnis': '',
    'Stärke (von 1-6)': '',
    'Konstitution (von 1-6)': '',
    'Intuition (von 1-6)': '',
    'Reaktion (von 1-6)': '',
    'Geschicklichkeit (von 1-6)': '',
    'Willenskraft (von 1-6)': '',
    'Glück (von 1-6)': '',
    'Magie (von 0-6)': '',
    'Resonanz (von 0-6)': ''
}

"""
What attributes describes the visual appearance. The content of this will be translated to english and then send to the image generator.
"""
UNTRANSLATED_APPEARANCE_ATTRIBUTE = 'Detailliertes Aussehen'


'''
midjourney adds the username in front of the image name. We need the name in order to remove it.
'''
MIDJOURNEY_USERNAME = 'Leto'