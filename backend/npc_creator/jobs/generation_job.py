import logging
import time
from threading import Thread

from npc_creator import config
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.download_image import DownloadImage
from npc_creator.operations.pass_image_prompt import PassImagePrompt
from npc_creator.repositories import npc_repo


def generation_job(generation_id: int) -> None:
    logging.debug(f'DownloadImageJob({generation_id}): Started')
    generation = ImageGeneration.objects.get(pk=generation_id)

    if generation.state == ImageGeneration.State.CREATED:
        result = PassImagePrompt(generation).call()
        logging.debug(f'DownloadImageJob({generation.id}): PassImagePrompt Operation {result}')

    if generation.state == ImageGeneration.State.IN_PROGRESS:
        result = DownloadImage(generation).call()
        logging.debug(f'DownloadImageJob({generation.id}): DownloadImage Operation {result}')

    if generation.state == ImageGeneration.State.IN_PROGRESS and generation.retry_count < config.MIDJOURNEY_RETRIES_BEFORE_FAILING:
        time.sleep(40 + pow(3, generation.retry_count))
        generation.retry_count += 1
        generation_job_async(generation)


def generation_job_async(generation: ImageGeneration) -> None:
    t = Thread(target=generation_job, args=[generation.id])
    t.start()
