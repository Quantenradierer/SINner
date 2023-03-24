import logging
import time
from threading import Thread

from npc_creator.operations.recreate_image import RecreateImage
from npc_creator.repositories import npc_repo


def recreate_missing_images() -> None:
    """
    Downloads an image for the given NPC ID and saves it in the NPC repository.

    Parameters
    ----------

    Returns
    -------
    None
    """

    logging.debug(f'RecreateMissingImages(): Started')
    for npc in npc_repo.requires_image_recreation():
        logging.debug(f'RecreateMissingImages: Started for {npc.id}')
        result = RecreateImage(npc).call()
        logging.debug(f'RecreateMissingImages: Finished for {npc.id} with result {result}')
        time.sleep(300)

def recreate_missing_images_async() -> None:
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
    t = Thread(target=recreate_missing_images)
    t.start()
