import asyncio
import json
import logging
import os
import re
import time
from threading import Event
from dataclasses import dataclass

import websockets

from npc_creator.operations import DownloadImage
from npc_creator.services.midjourney.find_correlated_response import MIDJOURNEY_BOT_ID


@dataclass
class Message:
    message: dict

    @property
    def op(self):
        return self.message.get("op", None)

    @property
    def d(self):
        return self.message.get("d", None)

    def is_midjourney(self):
        data = self.d
        if type(data) is not dict:
            return False

        author = data.get("author", {})
        return author.get("id", {}) == MIDJOURNEY_BOT_ID

    def is_message_update(self):
        return self.message.get("t", "") == "MESSAGE_UPDATE"

    def is_message_create(self):
        return self.message.get("t", "") == "MESSAGE_CREATE"

    def is_right_channel(self):
        data = self.d
        if type(data) is not dict:
            return False

        channel_id = data.get("channel_id", {})
        return channel_id == os.getenv("MJ_PRIVATE_DISCORD_CHANNEL_ID")

    def seed(self):
        result = re.findall(r"--seed (\d+)", self.d["content"])

        # da findall gibt Liste der alle gefundenen Werte zurück, nehmen wir den ersten
        if len(result) > 0:
            return int(result[0])

    def png_attachment(self):
        data = self.d
        if type(data) is not dict:
            return False

        if len(self.d.get("attachments", [])) == 0:
            return

        attachment = self.d["attachments"][0]
        if attachment.get("content_type", None) != "image/png":
            return

        return attachment.get("url", None)


URI = "wss://gateway.discord.gg/?v=6&encoding=json"
MAX_SIZE = 1024 * 1024 * 10
MAX_RETRIES = 5

CONNECT_PAYLOAD = {
    "op": 2,
    "d": {
        "token": os.getenv("MJ_PRIVATE_DISCORD_TOKEN"),
        "capabilities": 16381,
        "properties": {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "de-DE",
            "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "browser_version": "119.0.0.0",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 250836,
            "client_event_source": None,
        },
        "presence": {
            "status": "online",
            "since": 0,
            "activities": [],
            "afk": False,
        },
        "compress": False,
        "client_state": {
            "guild_versions": {},
            "highest_last_message_id": "0",
            "read_state_version": 0,
            "user_guild_settings_version": -1,
            "user_settings_version": -1,
            "private_channels_version": "0",
            "api_code_version": 0,
        },
    },
}


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Discord(metaclass=SingletonMeta):
    connected = False

    def __init__(self):
        self.websocket = None
        self.event = Event()

    def __enter__(self):
        logging.info("discord websocket: connect")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        self.websocket = loop.run_until_complete(
            websockets.connect(URI, max_size=MAX_SIZE)
        )
        loop.run_until_complete(self.websocket.send(json.dumps(CONNECT_PAYLOAD)))
        self.__class__.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info("discord websocket: disconnect")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.websocket.close())
        self.websocket = None
        self.__class__.connected = False

    def process(self):
        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        while True:
            try:
                message = Message(
                    json.loads(loop.run_until_complete(self.websocket.recv()))
                )
            except websockets.exceptions.WebSocketException as e:
                logging.info("discord websocket error", e)
                return True

            if message.op == 10:
                logging.info(f"discord websocket: message {message.d}")
                loop.create_task(self.send_heartbeat(message.d["heartbeat_interval"]))
            if message.op == 0:
                self.dispatch(message)

    def dispatch(self, message):
        if (
            message.is_right_channel()
            and message.is_midjourney()
            and message.is_message_create()
            and message.png_attachment()
            and message.seed()
        ):
            from npc_creator.models import ImageGeneration

            if ImageGeneration.objects.panel_exists(message.png_attachment()):
                return

            generation = ImageGeneration.objects.get(pk=message.seed())
            generation.url = message.png_attachment()
            DownloadImage(generation).call()
            generation.save()

    async def send_heartbeat(self, interval):
        while True:
            logging.info("discord websocket: sending heartbeat")
            await asyncio.sleep(interval / 1000)
            await self.websocket.send('{"op": 1, "d": null}')


def discord_websocket_main():
    reconnect = True
    while reconnect:
        if Discord.connected:
            break

        with Discord() as discord:
            discord.process()
            if not reconnect:
                break
            time.sleep(60)


def discord_websocket_main_job():
    discord_websocket_main()


if __name__ == "__main__":
    discord_websocket_main()
