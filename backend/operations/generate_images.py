import random
import time

from backend.repositories.npc import NpcRepository
from backend.services.discord_bot import pass_prompt

if __name__ == '__main__':
    repo = NpcRepository()
    npcs = repo.requires_image()
    print(npcs)
    for npc in npcs:
        pass_prompt(npc.image_generator_description + ' With some inspiration of Shadowrun.')
        npc.image_generation_started()
        repo.save(npc)

        # break
        time.sleep(200 + random.randint(-60, 60))

    # WIP: you still need to copy them into data/midjourney and then call services/midjourney_images.py