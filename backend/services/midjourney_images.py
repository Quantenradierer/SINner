import os.path

from PIL import Image


def split_image(image_path, output_path):
    im = Image.open(image_path)
    filename, file_extension = os.path.splitext(os.path.basename(image_path))

    width, height = im.size

    enumerator = 0
    for [x, y] in [[0, 0], [0, height / 2], [width / 2, 0], [width / 2, height / 2]]:
        enumerator += 1
        left = x
        top = y
        right = x + width / 2
        bottom = y + height / 2

        new_filename = filename + f'-{enumerator}' + file_extension
        splitted_file_path = os.path.join(output_path, new_filename)
        im.crop((left, top, right, bottom)).save(splitted_file_path)
        yield new_filename
    os.remove(image_path)
