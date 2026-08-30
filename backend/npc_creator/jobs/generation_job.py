import asyncio
import logging
import time
from threading import Thread

from discord_websocket import discord_websocket_main, discord_websocket_main_job
from npc_creator import config
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.download_image import DownloadImage
from npc_creator.operations.gpt.npc.pass_image_prompt import PassImagePrompt
from npc_creator.services.image_generation.find_correlated_response import (
    find_correlated_responses,
)
from npc_creator.services.image_generation.retrieve_latest_messages import (
    retrieve_latest_messages,
)


def generation_job(generation_id: int) -> None:
    """Thread entry point: never let an exception vanish into a dead daemon
    thread. On failure, mark the generation FAILED so the UI stops polling
    forever and the cause shows up in the logs."""
    try:
        _run_generation_job(generation_id)
    except Exception:
        logging.exception(f"DownloadImageJob({generation_id}): failed")
        ImageGeneration.objects.filter(pk=generation_id).exclude(
            state__in=[ImageGeneration.State.DOWNLOADED, ImageGeneration.State.DONE]
        ).update(state=ImageGeneration.State.FAILED)


def advance_generation(generation: ImageGeneration) -> None:
    """Move a generation one step forward, without any retry/backoff:
    kick off the image prompt when it is still CREATED, or look for a
    finished Midjourney grid and download it when it is IN_PROGRESS."""
    entity = generation.entity.instance

    if generation.state == ImageGeneration.State.CREATED:
        result = entity.PassImagePrompt(generation).call()
        logging.debug(
            f"DownloadImageJob({generation.id}): PassImagePrompt Operation {result}"
        )

    if generation.state == ImageGeneration.State.IN_PROGRESS:
        if not generation.url:
            responses = retrieve_latest_messages()
            for url in find_correlated_responses(responses, generation.id):
                if not ImageGeneration.objects.panel_exists(url):
                    generation.url = url
                    break

        if generation.url:
            result = DownloadImage(generation).call()
            logging.debug(
                f"DownloadImageJob({generation.id}): DownloadImage Operation {result}"
            )


def _run_generation_job(generation_id: int) -> None:
    logging.debug(f"DownloadImageJob({generation_id}): Started")
    generation = ImageGeneration.objects.get(pk=generation_id)

    advance_generation(generation)

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
