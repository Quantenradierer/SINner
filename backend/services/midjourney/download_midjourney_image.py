import requests
import os


def download_midjourney_image(save_path: str, url: str) -> str:
    """
    Download an image from the given URL and save it in a local directory.

    Parameters
    ----------
    url : str
        The URL of the image to be downloaded.

    Returns
    -------
    str
        The local path where the image was saved.

    Raises
    ------
    requests.exceptions.RequestException
        If there is an error while making the request to download the image.

    IOError
        If there is an error while writing the image to the local directory.

    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return None

    local_path = os.path.join(save_path, os.path.basename(url))

    with open(local_path, "wb") as f:
        f.write(response.content)
    return local_path
