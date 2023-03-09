from functools import cache


@cache
def banned_words():
    with open('data/midjourney_banned_words.txt') as file:
        banned_words = file.readlines()
    return [' ' + word.strip().lower() + ' ' for word in banned_words if word.strip()]


def contains_banned_word(text):
    text = text.lower()
    for word in banned_words():
        if word in text:
            return True
    return False

