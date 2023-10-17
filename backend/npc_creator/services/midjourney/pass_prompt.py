import os
import shadowrun.settings
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
               "channel_id": CHANNEL_ID, "session_id": "b36c5d147f15d2547e9fb0384bdb4811",
               "data": {"version": "1118961510123847772", "id": "938956540159881230", "name": "imagine", "type": 1,
                        "options": [{"type": 3, "name": "prompt", "value": prompt}],
                        "application_command": {"id": "938956540159881230",
                                                "application_id": "936929561302675456",
                                                "version": "1118961510123847772",
                                                "default_member_permissions": None,
                                                "type": 1, "nsfw": False, "name": "imagine",
                                                "description": "Create images with Midjourney",
                                                "dm_permission": True,
                                                "contexts": [0, 1, 2],
                                                "integration_types": [0],
                                                "options": [{"type": 3, "name": "prompt",
                                                             "description": "The prompt to imagine",
                                                             "required": True}]},
                        "attachments": []}}


    header = {
        'authorization': PRIVATE_DISCORD_TOKEN
    }
    try:
        response = requests.post("https://discord.com/api/v9/interactions", json=payload, headers=header)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False


if __name__ == '__main__':
    assert(SERVER_ID != None)
    assert(CHANNEL_ID != None)
    assert(pass_prompt('In a cyberpunk/shadowrun: A human with a suit.') == True)
