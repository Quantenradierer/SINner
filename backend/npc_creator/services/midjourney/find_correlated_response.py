from typing import Optional, List, Dict

MIDJOURNEY_BOT_ID = '936929561302675456'


def find_correlated_responses(responses: List[Dict[str, any]], search_text: List[str]) -> List[str]:
    """
    Search for a response message in a list of messages based on the given search text.

    Parameters
    ----------
    responses : List[Dict[str, any]]
        List of message response dictionaries to search through.
    search_text : str
        The text to search for in the message content.

    Returns
    -------
    List[str]
        a list of URLs for all messages that matches the search criteria and contains a PNG attachment
    """
    if not search_text.strip():
        return []

    for message in responses:
        if not all(key in message for key in ['content', 'author', 'attachments']) or 'id' not in message['author']:
            continue

        if search_text not in message['content']:
            continue
        if message['author']['id'] != MIDJOURNEY_BOT_ID and 'OVERRIDE' not in message['content']:
            continue
        if not message['attachments'] or 'url' not in message['attachments'][0]:
            continue

        url = message['attachments'][0]['url']
        if not url.lower().endswith('.png'):
            continue

        yield url
    return []
