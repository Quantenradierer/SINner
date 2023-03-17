import os.path

import PIL
from PIL import Image


def split_image(image_path: str, output_path: str) -> list[str]:
    """
    Splits an image into 4 equally sized parts and saves each part as a separate file in the specified output directory.

    Args:
        image_path (str): Path to the image file to be split.
        output_path (str): Path to the output directory where the splitted files will be saved.

    Returns:
        List[str]: A list of the filenames of the splitted files.

    """
    try:
        im = Image.open(image_path)
    except PIL.UnidentifiedImageError:
        return []
    filename, file_extension = os.path.splitext(os.path.basename(image_path))

    width, height = im.size

    result = []
    for x, y in [[0, 0], [0, height // 2], [width // 2, 0], [width // 2, height // 2]]:
        left = x
        top = y
        right = x + width // 2
        bottom = y + height // 2

        new_filename = f"{filename}-{len(result)}{file_extension}"
        splitted_file_path = os.path.join(output_path, new_filename)
        im.crop((left, top, right, bottom)).save(splitted_file_path)
        result.append(new_filename)
    os.remove(image_path)
    return result
