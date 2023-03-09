import requests
import os

from repositories.npc import NpcRepository

SERVER_ID = os.getenv('MJ_SERVER_ID')
CHANNEL_ID = os.getenv('MJ_CHANNEL_ID')
PRIVATE_DISCORD_TOKEN = os.getenv('MJ_PRIVATE_DISCORD_TOKEN')
MIDJOURNEY_BOT_ID = '936929561302675456'


#{"type":2,"application_id":"936929561302675456","guild_id":"853338015502303263",
# "channel_id":"1015753074935083099","session_id":"9e394ea43e050cd23c98cbaed9bd53b8",
# "data":{"version":"1077969938624553050","id":"938956540159881230",
# "name":"imagine","type":1,"options":[{"type":3,"name":"prompt","value":"a giant cat spider"}],
# "application_command":{"id":"938956540159881230","application_id":"936929561302675456","version":"1077969938624553050",
# "default_permission":true,"default_member_permissions":null,"type":1,"nsfw":false,"name":"imagine",
# "description":"Create images with Midjourney","dm_permission":true,"options":
# [{"type":3,"name":"prompt","description":"The prompt to imagine","required":true}]},"attachments":[]},
# "nonce":"1083355138418016256"}
def pass_prompt(prompt: str):
    payload ={"type": 2, "application_id": "936929561302675456", "guild_id": SERVER_ID,
               "channel_id": CHANNEL_ID, "session_id": "9e394ea43e050cd23c98cbaed9bd53b8",
               "data": {"version": "1077969938624553050", "id": "938956540159881230", "name": "imagine", "type": 1,
                        "options": [{"type": 3, "name": "prompt", "value": prompt}],
                        "application_command": {"id": "938956540159881230",
                                                "application_id": "936929561302675456",
                                                "version": "1077969938624553050",
                                                "default_permission": True,
                                                "default_member_permissions": None,
                                                "type": 1, "nsfw": False, "name": "imagine",
                                                "description": "Create images with Midjourney",
                                                "dm_permission": True,
                                                "options": [{"type": 3, "name": "prompt",
                                                             "description": "The prompt to imagine",
                                                             "required": True}]},
                        "attachments": []}}

    header = {
        'authorization': PRIVATE_DISCORD_TOKEN
    }
    response = requests.post("https://discord.com/api/v9/interactions",
                             json=payload, headers=header)
    return response


def retrieve_latest_messages():
    # Discord API endpoint for channels
    url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

    headers = {
        "Authorization": PRIVATE_DISCORD_TOKEN,
        "Content-Type": "application/json"
    }

    params = {
        "limit": 50
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()


def download_midjourney_image(url):
    response = requests.get(url)
    local_path = f'data/midjourney/{os.path.basename(url)}'

    # Schreiben der Binärdaten in eine Datei
    with open(local_path, "wb") as f:
        f.write(response.content)
    return local_path


if __name__ == '__main__':
    # pass_prompt('just a test prompt')
    repo = NpcRepository()
    npc = repo.find(13)
    search_text = npc.image_generator_description

    response = retrieve_latest_messages()
    for message in response:
        if message['author']['id'] != MIDJOURNEY_BOT_ID:
            continue
        if search_text not in message['content']:
            continue

        url = message['attachments'][0]['url']
        path = download_midjourney_image(url)
        break