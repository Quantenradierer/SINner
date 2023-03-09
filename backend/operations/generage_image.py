import os.path
import time
from threading import Thread

from backend.repositories.npc import NpcRepository
from services.banned_words_filter import contains_banned_word
from services.midjourney import retrieve_latest_messages, MIDJOURNEY_BOT_ID, download_midjourney_image, pass_prompt
from services.midjourney_images import split_image


def find_correlated_response(responses, search_text):
    for message in responses:
        if message['author']['id'] != MIDJOURNEY_BOT_ID:
            continue
        if search_text not in message['content']:
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

    image_path = download_midjourney_image(url)
    splitted_file_names = list(split_image(image_path, os.path.join('frontend/public/images/npcs/')))
    return splitted_file_names[0]


def generate_image_job(npc_id):
    repo = NpcRepository()
    npc = repo.find(npc_id)

    if contains_banned_word(npc.image_generator_description):
        npc.image_generator_state = 'banned'
        repo.save(npc)
        return

    pass_prompt(f'In Shadowrun/Cyberpunk: {npc.image_generator_description}')
    npc.image_generation_started()
    for i in range(6):
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


if __name__ == '__main__':
    repo = NpcRepository()
    npcs = [repo.find(166),]# .requires_image_generation()[0:10]

    for npc in npcs:
        print(npc)
        generate_image_job(npc.id)

#        image_path = find_and_save_image(npc.image_generator_description)
#        if image_path:
#            npc.add_image(image_path)
#            repo.save(npc)
#            break