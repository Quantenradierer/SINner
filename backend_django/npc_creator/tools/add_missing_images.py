import time

from jobs.download_image import download_image_job
from operations.pass_image_prompt import PassImagePrompt
from repositories.npc import NpcRepository

if __name__ == '__main__':
    repo = NpcRepository()
    npcs = repo.requires_image_generation()
    for npc in npcs:
        PassImagePrompt(npc)
        download_image_job(npc.id)
        time.sleep(30)