import asyncio
import logging
import time
from threading import Thread

from discord_websocket import discord_websocket_main, discord_websocket_main_job
from npc_creator import config
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.download_image import DownloadImage
from npc_creator.operations.gpt.npc.pass_image_prompt import PassImagePrompt
from npc_creator.services.midjourney.find_correlated_response import (
    find_correlated_responses,
)
from npc_creator.services.midjourney.retrieve_latest_messages import (
    retrieve_latest_messages,
)


def generation_job(generation_id: int) -> None:
    logging.debug(f"DownloadImageJob({generation_id}): Started")
    generation = ImageGeneration.objects.get(pk=generation_id)

    entity = generation.entity.instance

    if generation.state == ImageGeneration.State.CREATED:
        result = entity.PassImagePrompt(generation).call()
        logging.debug(
            f"DownloadImageJob({generation.id}): PassImagePrompt Operation {result}"
        )

    if generation.state == ImageGeneration.State.IN_PROGRESS:
        responses = retrieve_latest_messages()
        urls = find_correlated_responses(responses, generation.id)

        for url in urls:
            if not ImageGeneration.objects.panel_exists(url):
                generation.url = url
                break

        result = DownloadImage(generation).call()
        logging.debug(
            f"DownloadImageJob({generation.id}): DownloadImage Operation {result}"
        )

    generation.refresh_from_db()
    if (
        generation.state == ImageGeneration.State.IN_PROGRESS
        and generation.retry_count < config.MIDJOURNEY_RETRIES_BEFORE_FAILING
    ):
        generation.retry_count += 1
        generation.save()

        time.sleep(600 + pow(4, generation.retry_count))
        generation.refresh_from_db()
        generation_job_async(generation)


def generation_job_async(generation: ImageGeneration) -> None:
    Thread(target=discord_websocket_main_job).start()
    Thread(target=generation_job, args=[generation.id]).start()
