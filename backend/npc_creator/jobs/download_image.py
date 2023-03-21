import time
from threading import Thread

from npc_creator import config
from npc_creator.operations.download_image import DownloadImage
from npc_creator.operations.pass_image_prompt import PassImagePrompt
from npc_creator.repositories import npc_repo


def download_image_job(npc_id: str) -> None:
    """
    Downloads an image for the given NPC ID and saves it in the NPC repository.

    Parameters
    ----------
    npc_id : str
        The ID of the NPC whose image is to be downloaded.

    Returns
    -------
    None
    """
    npc = npc_repo.find(npc_id)

    PassImagePrompt(npc).call()

    for i in range(config.MIDJOURNEY_RETRIES_BEFORE_FAILING):
        time.sleep(40 + pow(4, i))
        if DownloadImage(npc).call():
            break


def download_image_job_async(npc: object) -> None:
    """
    Starts a new thread to download an image for the given NPC object.

    Parameters
    ----------
    npc : object
        The NPC object whose image is to be downloaded.

    Returns
    -------
    None
    """
    return
    t = Thread(target=download_image_job, args=[npc.id])
    t.start()
