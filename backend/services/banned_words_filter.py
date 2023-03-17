from functools import cache
from typing import List

import config


@cache
def banned_words() -> List[str]:
    """
    Load and return a list of banned words from the 'midjourney_banned_words.txt' file.

    Returns:
        List[str]: List of banned words, where each word is surrounded by spaces and converted to lowercase.
    """
    with open(config.BANNED_WORD_FILE) as file:
        banned_words = file.readlines()
    return [' ' + word.strip().lower() + ' ' for word in banned_words if word.strip()]


def contains_banned_word(text: str) -> bool:
    """
    Check if the given text contains any banned words.

    Args:
        text (str): The text to check for banned words.

    Returns:
        bool: True if the text contains a banned word, False otherwise.
    """
    text = ' ' + text.lower() + ' '
    return any(word in text for word in banned_words())
