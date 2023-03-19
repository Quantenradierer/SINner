import os

import requests

SERVER_ID = os.getenv('MJ_SERVER_ID')
CHANNEL_ID = os.getenv('MJ_CHANNEL_ID')
PRIVATE_DISCORD_TOKEN = os.getenv('MJ_PRIVATE_DISCORD_TOKEN')


def pass_prompt(prompt: str) -> bool:
    """
    Sends a prompt to the Midjourney Discord bot using the Discord API.

    Args:
        prompt (str): The prompt to send to the bot.

    Returns:
        requests.models.Response: The response object returned by the Discord API.

    Raises:
        requests.exceptions.RequestException: If an error occures while sending the request

    """
    payload = {"type": 2, "application_id": "936929561302675456", "guild_id": SERVER_ID,
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
    try:
        response = requests.post("https://discord.com/api/v9/interactions", json=payload, headers=header)
    except requests.exceptions.RequestException:
        return False
    return response.status_code == 200
