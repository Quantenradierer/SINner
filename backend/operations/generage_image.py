import time
from threading import Thread

from repositories.npc import NpcRepository
from config import PUBLIC_NPC_IMAGE_PATH, MIDJOURNEY_PROMPT, MIDJOURNEY_RETRIES_BEFORE_FAILING
from services.banned_words_filter import contains_banned_word
from services.midjourney import retrieve_latest_messages, MIDJOURNEY_BOT_ID, download_midjourney_image, pass_prompt
from services.midjourney_images import split_image


def find_correlated_response(responses, search_text):
    for message in responses:
        if message['author']['id'] != MIDJOURNEY_BOT_ID:
            continue
        if search_text not in message['content']:
            continue
        if not message['attachments']:
            continue

        url = message['attachments'][0]['url']
        if not url.lower().endswith('.png'):
            continue

        return url


def find_and_crop_image(image_generator_description):
    responses = retrieve_latest_messages()
    url = find_correlated_response(responses, image_generator_description)
    if not url:
        return False

    image_name = download_midjourney_image(url)
    splitted_file_names = list(split_image(image_name, PUBLIC_NPC_IMAGE_PATH))
    return splitted_file_names[0]


def generate_image_job(npc_id):
    repo = NpcRepository()
    npc = repo.find(npc_id)

    if contains_banned_word(npc.image_generator_description):
        npc.image_generator_state = 'banned'
        repo.save(npc)
        return

    pass_prompt(MIDJOURNEY_PROMPT.format(image_generator_description=npc.image_generator_description))
    npc.image_generation_started()
    repo.save(npc)
    for i in range(MIDJOURNEY_RETRIES_BEFORE_FAILING):
        time.sleep(40 + pow(4, i))
        image_path = find_and_crop_image(npc.image_generator_description)
        if image_path:
            npc.add_image(image_path)
            repo.save(npc)
            break
    else:
        npc.image_generator_state = 'failed'
        repo.save(npc)


def generate_image_job_async(npc):
    t = Thread(target=generate_image_job, args=[npc.id])
    t.start()
