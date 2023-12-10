import os.path
import uuid
from urllib.parse import urlparse

from npc_creator import config
from npc_creator.models.image import Image
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.return_types import Failure, Success, ReturnType
from npc_creator.services.midjourney.download_midjourney_image import (
    download_midjourney_image,
)

from npc_creator.services.midjourney.split_images import split_image


class DownloadImage:
    def __init__(self, generation: ImageGeneration, temp_image_path="data/midjourney/"):
        """
        Constructor of the GenerateImage class.
        """

        self.generation = generation
        self.entity = self.generation.entity
        self.temp_image_path = temp_image_path

    def call(self) -> ReturnType:
        """
        downloads and saves the image to the npc

        Returns:
            ReturnType: True if the image was successfully saved, False otherwise.
        """
        result_image_paths = self.download_images()
        if not result_image_paths:
            return result_image_paths

        self.add_images(result_image_paths.data)
        self.entity.save()

        self.generation.state = ImageGeneration.State.DOWNLOADED
        self.generation.save()
        return result_image_paths

    def add_images(self, image_paths):
        for name in image_paths:
            Image.objects.create(
                entity=self.entity, name=name, generation=self.generation
            )

    def plural_entity_type(self):
        return self.entity.kind.lower() + "s"

    def download_images(self):
        panel_name = os.path.basename(urlparse(self.generation.url).path)

        panel_image_path = os.path.join(self.temp_image_path, panel_name)
        success = download_midjourney_image(panel_image_path, url=self.generation.url)
        if not success:
            return Failure("download of midjourney image failed")

        image_names = split_image(
            panel_image_path,
            self.images_names_iterator(self.plural_entity_type()),
        )
        return Success(image_names)

    @staticmethod
    def images_names_iterator(entity_type):
        while True:
            yield os.path.join(
                config.PUBLIC_ENTITY_IMAGE_PATH, entity_type, str(uuid.uuid1()) + ".png"
            )
