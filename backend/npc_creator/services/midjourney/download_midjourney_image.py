import os
from typing import Optional

import requests


def download_midjourney_image(save_path: str, url: str) -> Optional[str]:
    """
    Download an image from the given URL and save it in a local directory.

    Parameters
    ----------
    save_path : str
        The path to the directory where the downloaded image will be saved.
    url : str
        The URL of the image to download.

    Returns
    -------
    str
        If the image is downloaded and saved successfully, returns the full
        path to the saved image on the local filesystem. If an error occurs,
        returns an empty string.
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return False

    with open(save_path, "wb") as f:
        f.write(response.content)
    return True
