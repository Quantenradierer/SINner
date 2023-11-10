import random
import time

from npc_creator.services.midjourney.pass_prompt import pass_prompt
from npc_creator.services.special_midjourney_prompt import special_midjourney_prompt


from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        amount = (
            2
            + random.randint(0, 1)
            + random.randint(0, 1)
            + random.randint(0, 1)
            + random.randint(0, 1)
        )

        for i in range(amount):
            # male_template = example_image.find('troll_male')
            prompt = f'In Shadowrun/Cyberpunk: A 38-year-old of English background ethnicity. An orc who works as an illegal fighting organizer. The orc named "Bonebreaker" is 1.90 meters tall and weighs just under 140 kg, with most of his mass consisting of muscle. His skull is noticeably larger than the normal human skull, and he has dense black hair, which he usually wears in a frayed mohawk. He has a scar on his left eye and his skin is covered in numerous tattoos.'
            # {male_template.url}

            prompt = special_midjourney_prompt(prompt, metatyp="Ork", gender="männlich")
            pass_prompt(prompt)
            print(prompt)

            sleeptime = (
                random.randint(0, 100) / 100
                + 2
                + random.randint(0, 3)
                + random.randint(0, 3)
                + random.randint(0, 3)
                + random.randint(0, 2)
                + random.randint(0, 1)
                + random.randint(0, 1)
                + random.randint(0, 1)
                + random.randint(0, 1)
            )
            time.sleep(sleeptime)
