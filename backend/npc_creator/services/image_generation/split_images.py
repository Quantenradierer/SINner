import io
import os.path
from typing import List

import PIL
from PIL import Image


def split_image_to_bytes(image_path: str) -> List[bytes]:
    """Split a Midjourney 2x2 grid into its four quadrants.

    Returns the four quadrants as PNG-encoded bytes and deletes the source
    file. Returns an empty list if the source is not a readable image.
    """
    try:
        im = Image.open(image_path)
    except PIL.UnidentifiedImageError:
        return []

    width, height = im.size
    half_w, half_h = width // 2, height // 2
    offsets = [(0, 0), (half_w, 0), (0, half_h), (half_w, half_h)]

    quadrants = []
    for x, y in offsets:
        buffer = io.BytesIO()
        im.crop((x, y, x + half_w, y + half_h)).save(buffer, "PNG")
        quadrants.append(buffer.getvalue())

    os.remove(image_path)
    return quadrants
