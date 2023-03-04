from PIL import Image
import os.path

from backend.repositories.npc import NpcRepository


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
        print(output_path, splitted_file_path, filename)
        im.crop((left, top, right, bottom)).save(splitted_file_path)
        yield new_filename
    os.remove(image_path)


if __name__ == '__main__':
    output_path = 'frontend/public/images/npcs'
    input_path = 'data/midjourney'

    for beginning_size in range(63, 15, -1):
        repo = NpcRepository()
        for root, folder, files in os.walk(input_path):
            for file in files:
                beginning = file[5:beginning_size].replace('_', ' ')
                npc = repo.find_image_description(beginning)
                if npc:
                    splitted_file_names = list(split_image(image_path=os.path.join(root, file), output_path=output_path))
                    npc.add_image(f'./images/npcs/{splitted_file_names[0]}')
                    repo.save(npc)

