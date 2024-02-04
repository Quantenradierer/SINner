import os

import PIL
from PIL import Image


def create_thumbnail(image_path: str) -> bool:
    """
    Creates a thumbnail of the image at the specified path.

    Args:
        image_path (str): Path to the image file to be thumbnailed.

    Returns:
        bool: True if the thumbnail was created successfully, False otherwise.

    """

    if not image_path.endswith(".png"):
        image_path += ".png"

    extensionless_image_path = os.path.splitext(image_path)[0]

    thumbnail_path = os.path.join(
        os.path.dirname(extensionless_image_path),
        "jpgs",
        os.path.basename(extensionless_image_path) + ".jpg",
    )

    if os.path.exists(os.path.dirname(thumbnail_path)):
        return True

    try:
        im = Image.open(image_path)
    except (PIL.UnidentifiedImageError, FileNotFoundError):
        return False

    os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
    im.save(thumbnail_path, "JPEG")
    return True
