import time
from threading import Thread

from npc_creator import config
from npc_creator.operations.download_image import DownloadImage
from npc_creator.operations.pass_image_prompt import PassImagePrompt

from npc_creator.repositories import npc_repo


#from npc_creator.operations.pass_image_prompt import PassImagePrompt
#from npc_creator.repositories.npc import NpcRepository


def download_image_job(npc_id):
    npc = npc_repo.find(npc_id)

    PassImagePrompt(npc).call()
    npc_repo.save(npc)

    for i in range(config.MIDJOURNEY_RETRIES_BEFORE_FAILING):
        time.sleep(40 + pow(4, i))
        if DownloadImage(npc).call():
            break


def download_image_job_async(npc):
    t = Thread(target=download_image_job, args=[npc.id])
    t.start()
