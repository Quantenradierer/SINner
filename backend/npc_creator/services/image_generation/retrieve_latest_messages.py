import os

import requests

SERVER_ID = os.getenv("MJ_SERVER_ID")
CHANNEL_ID = os.getenv("MJ_CHANNEL_ID")
PRIVATE_DISCORD_TOKEN = os.getenv("MJ_PRIVATE_DISCORD_TOKEN")


def retrieve_latest_messages():
    # Discord API endpoint for channels
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

    headers = {
        "Authorization": PRIVATE_DISCORD_TOKEN,
        "Content-Type": "application/json",
    }

    params = {"limit": 50}

    try:
        response = requests.get(url, headers=headers, params=params)
    except requests.exceptions.RequestException:
        return []
    if response.status_code != 200:
        return []
    return response.json()
