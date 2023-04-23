import os.path
from typing import List

import PIL
from PIL import Image


def split_image(image_path: str, image_paths_iter: List[str]) -> List[str]:
    """
    Splits an image into 4 equally sized parts and saves each part as a separate file in the specified output directory.

    Args:
        image_path (str): Path to the image file to be split.
        image_paths_iter (str): pathes where to save the items

    Returns:
        List[str]: A list of the filenames of the splitted files.

    """
    try:
        im = Image.open(image_path)
    except PIL.UnidentifiedImageError:
        return []

    width, height = im.size

    result = []

    splits = [[0, 0], [width // 2, 0], [0, height // 2], [width // 2, height // 2]]
    for (x, y), file_path in zip(splits, image_paths_iter):
        left = x
        top = y
        right = x + width // 2
        bottom = y + height // 2

        im.crop((left, top, right, bottom)).save(file_path)
        result.append(os.path.basename(file_path))
    os.remove(image_path)
    return result
