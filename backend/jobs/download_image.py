import time
from threading import Thread

import config
from operations.download_image import DownloadImage
from repositories.npc import NpcRepository


def download_image_job(npc_id):
    repo = NpcRepository()
    npc = repo.find(npc_id)
    for i in range(config.MIDJOURNEY_RETRIES_BEFORE_FAILING):
        time.sleep(40 + pow(4, i))
        if DownloadImage(npc).call():
            break


def download_image_job_async(npc):
    t = Thread(target=download_image_job, args=[npc.id])
    t.start()
