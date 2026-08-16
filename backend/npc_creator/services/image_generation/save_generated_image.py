import os
import uuid

from npc_creator.services.image_generation.create_thumbnails import create_thumbnail
from npc_creator.utils import entity_directory


def save_generated_image(image_bytes: bytes, entity_kind: str) -> str:
    """
    Saves raw image bytes as a new entity image file and creates its thumbnail.

    Returns:
        str: the extensionless file name, matching the convention used for
        entity images elsewhere (see split_image / Image.name).
    """
    directory = entity_directory(entity_kind)
    os.makedirs(directory, exist_ok=True)

    name = str(uuid.uuid1())
    file_path = os.path.join(directory, name)
    with open(file_path + ".png", "wb") as f:
        f.write(image_bytes)

    create_thumbnail(file_path)
    return name
