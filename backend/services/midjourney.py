import requests
import os


SERVER_ID = os.getenv('MJ_SERVER_ID')
CHANNEL_ID = os.getenv('MJ_CHANNEL_ID')
PRIVATE_DISCORD_TOKEN = os.getenv('MJ_PRIVATE_DISCORD_TOKEN')


def pass_prompt(prompt: str):
    payload ={"type": 2, "application_id": "936929561302675456", "guild_id": SERVER_ID,
               "channel_id": CHANNEL_ID, "session_id": "2fb980f65e5c9a77c96ca01f2c242cf6",
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






if __name__ == '__main__':
    pass_prompt('just a test prompt')

