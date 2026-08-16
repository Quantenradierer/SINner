import requests


def download_midjourney_image(save_path: str, url: str) -> bool:
    """
    Download an image from the given URL and save it to the given file path.

    Parameters
    ----------
    save_path : str
        The full file path where the downloaded image will be saved.
    url : str
        The URL of the image to download.

    Returns
    -------
    bool
        True if the image was downloaded and saved successfully, False if
        the request failed.
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return False

    with open(save_path, "wb") as f:
        f.write(response.content)
    return True
