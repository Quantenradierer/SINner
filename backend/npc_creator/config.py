import logging
import os
import sys

import openai
import requests


logging.basicConfig(filename="schattenakte.log")
logging.getLogger().setLevel(logging.DEBUG)

"""
file for the database
"""
SQLITE_FILE = "data/npcs.sqlite"

"""
directory for npc images
"""
PUBLIC_NPC_IMAGE_PATH = os.getenv("PUBLIC_NPC_IMAGE_PATH")

"""
file for 
"""
BANNED_WORD_FILE = "data/midjourney_banned_words.txt"


"""
The images from midjourney will be saved temporary in this directory
"""
MIDJOURNEY_TEMP_PATH = "data/midjourney"

"""
the prompt for midjourney
"""
MIDJOURNEY_PROMPT = "In Shadowrun/Cyberpunk: {image_generator_description}"
ADDITIONAL_PROMPT_OPTIONS = "--ar 4:5"

"""
how often it shall be tried. The time between every try it calculated with '40 + pow(3, i)'
Means the waiting time is: 31s, 46s, 94s, ~5min, ~17min, ~68min.
After all this time the image generation counts as 'failed'.
This often happens when the image generation contains bad words, where the image couldn't get generated
"""
MIDJOURNEY_RETRIES_BEFORE_FAILING = 8

# noinspection PyPep8


"""
configuration for openai
"""
openai.api_key = os.getenv("OPENAI_API_KEY")


if "test" in sys.argv:

    def mock(*args, **kwargs):
        raise Exception("if this has raised in your test, your mocks do not work.")

    openai.create = mock
    requests.get = mock
    requests.post = mock
