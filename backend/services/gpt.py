import logging

import openai
import os

from backend.factories.npc_from_gpt import npc_from_gpt
from backend.repositories.npc import NpcRepository, Npc


PROMPT = """
Erstelle einen Shadowrun NPC mit den folgenden Attributen:

"""

visual_style = '''
Name:
Metatype:
Beruf:
Ethnizität:
Geschlecht:
Alter:
Geruch:
Detailliertes Aussehen:
Detailliertes Aussehen (english):
'''

social = '''
Kontakte:
Stärken:
Schwächen:
Eigenarten:
Hobbys und Interessen: 
'''

background = '''
Background-Story:
Erfahrungen:
Ressentiments:
Motivationen:
Ziele:
'''

skills = '''
Fertigkeiten:
Ausrüstung:
Ruf:
Geld:
Ressourcen:
'''

attributes = '''
Stärke (von 1-6):
Konstitution (von 1-6):
Intuition (von 1-6):
Reaktion (von 1-6):
Geschicklichkeit (von 1-6):
Willenskraft (von 1-6):
Glück (von 1-6):
Magie (von 0-6):
Resonanz (von 0-6):
'''



class Gpt:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def ask_gpt(self, prompt):
        logging.info(f'GPT Prompt: {prompt}')
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=512)
        logging.info(f'GPT Response: {response}')
        return response['choices'][0]['text']

    def ask_chatgpt(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
#            messages=[{"role": 'system', 'content': 'Create various different Shadowrun NPCs with the'}],
            messages=[{"role": "user", "content": prompt}]
        )

        print(completion)


if __name__ == '__main__':
    gpt = Gpt()
    prompt = PROMPT + social + background + skills + visual_style
    print(prompt) # gpt.ask_chatgpt(prompt)


    '''
        npc_repo = NpcRepository()
        gpt = Gpt()
        for i in range(10):
            gpt_answer = gpt.ask(PROMPT)
            npc = npc_from_gpt(gpt_answer)
            npc_repo.create(npc)
        #print(gpt.ask(PROMPT))
    '''