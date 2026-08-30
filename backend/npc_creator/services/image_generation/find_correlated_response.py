import re
from typing import Optional, List, Dict
from urllib.parse import urlparse

MIDJOURNEY_BOT_ID = "936929561302675456"

# Midjourney has shipped grid attachments as .png and (since ~v6) .webp.
IMAGE_EXTENSIONS = (".png", ".webp", ".jpg", ".jpeg")


def _is_image_attachment(attachment: Dict[str, any]) -> bool:
    if str(attachment.get("content_type", "")).startswith("image/"):
        return True
    return urlparse(attachment.get("url", "")).path.lower().endswith(IMAGE_EXTENSIONS)


def find_correlated_responses(
    responses: List[Dict[str, any]], search_seed: int
) -> List[str]:
    """
    Search for a response message in a list of messages based on the given search text.

    Parameters
    ----------
    responses : List[Dict[str, any]]
        List of message response dictionaries to search through.
    search_seed : int
        seed which shall be searched

    Returns
    -------
    List[str]
        a list of URLs for all messages that matches the search criteria and contains an image attachment
    """
    if not search_seed:
        return []

    for message in responses:
        if (
            not all(key in message for key in ["content", "author", "attachments"])
            or "id" not in message["author"]
        ):
            continue

        if not re.search(rf"--seed {search_seed}(?!\d)", message["content"]):
            continue
        if (
            message["author"]["id"] != MIDJOURNEY_BOT_ID
            and "OVERRIDE" not in message["content"]
        ):
            continue
        if not message["attachments"] or "url" not in message["attachments"][0]:
            continue

        attachment = message["attachments"][0]
        if not _is_image_attachment(attachment):
            continue

        yield attachment["url"]
    return []
