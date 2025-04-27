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
PUBLIC_ENTITY_IMAGE_PATH = os.getenv("PUBLIC_IMAGE_PATH")

"""
file for 
"""
BANNED_WORD_FILE = "data/midjourney_banned_words.txt"


"""
The images from midjourney will be saved temporary in this directory
"""
MIDJOURNEY_TEMP_PATH = "data/midjourney"


"""
how often it shall be tried. The time between every try it calculated with '40 + pow(3, i)'
Means the waiting time is: 31s, 46s, 94s, ~5min, ~17min, ~68min.
After all this time the image generation counts as 'failed'.
This often happens when the image generation contains bad words, where the image couldn't get generated
"""
MIDJOURNEY_RETRIES_BEFORE_FAILING = 8

# noinspection PyPep8


if "test" in sys.argv:

    def mock(*args, **kwargs):
        raise Exception("if this has raised in your test, your mocks do not work.")

    openai.create = mock
    requests.get = mock
    requests.post = mock
