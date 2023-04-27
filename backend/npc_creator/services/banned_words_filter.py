from functools import cache
from typing import List
import re

from npc_creator import config


@cache
def banned_words_regex() -> List[str]:
    """
    Load and return a list of banned words from the 'midjourney_banned_words.txt' file.

    Returns:
        List[str]: List of banned words as regex, where each word is surrounded by spaces and converted to lowercase.
    """
    with open(config.BANNED_WORD_FILE) as file:
        words = file.readlines()
    return [re.compile(f'(?i)[.,\-"\' ]{word.strip().lower()}[.,\-"\' ]') for word in words if word.strip()]


def remove_banned_words(text: str) -> bool:
    """
    Check if the given text contains any banned words.

    Args:
        text (str): The text to check for banned words.

    Returns:
        bool: True if the text contains a banned word, False otherwise.
    """
    text = ' ' + text + ' '
    for regex in banned_words_regex():
        match = regex.search(text)
        if match:
            text = text[:match.span()[0] + 1] + text[match.span()[1] - 1:]

    text = text.replace('  ', ' ')
    return text.strip()
