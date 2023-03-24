import logging
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

    logging.debug(f'DownloadImageJob({npc_id}): Started')
    npc = npc_repo.find(npc_id)

    result = PassImagePrompt(npc).call()
    logging.debug(f'DownloadImageJob({npc_id}): PassImagePrompt Operation {result}')

    for i in range(config.MIDJOURNEY_RETRIES_BEFORE_FAILING):
        time.sleep(40 + pow(4, i))
        result = DownloadImage(npc).call()
        logging.debug(f'DownloadImageJob({npc_id}): DownloadImage Operation {result}')
        if result:
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
    t = Thread(target=download_image_job, args=[npc.id])
    t.start()
