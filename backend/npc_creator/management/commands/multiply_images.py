import random
import time

from npc_creator.services.midjourney.pass_prompt import pass_prompt
from npc_creator.services.special_midjourney_prompt import special_midjourney_prompt


from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        amount = 2 + random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1)

        for i in range(2):
            #male_template = example_image.find('troll_male')
            prompt = f'In Shadowrun, a female troll' # {male_template.url}

            prompt = special_midjourney_prompt(prompt, metatyp='Troll', gender='weiblich')
            pass_prompt(prompt)
            print(prompt)
            sleeptime = random.randint(0, 100) / 100 + 2 + random.randint(0, 3) + random.randint(0, 3) + random.randint(0, 3) + random.randint(0, 2) + random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1)
            #print(sleeptime)
            time.sleep(sleeptime)
            # minotaur:: fur::-0.1 animal::-0.1 monster::-0.1
            # female troll:: female:: minotaur:: wrinkles:: small horns:: fur::-0.3 beard::-0.3

