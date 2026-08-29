import os.path
from urllib.parse import urlparse

from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.return_types import Failure, Success, ReturnType
from npc_creator.services.image_generation.download_midjourney_image import (
    download_midjourney_image,
)
from npc_creator.services.image_generation.factory import ImageGeneratorFactory
from npc_creator.services.image_generation.split_images import split_image_to_bytes
from npc_creator.services.image_generation.store_image import store_entity_image


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
        result = self.download_images()
        if not result:
            return result

        self.entity.save()

        self.generation.state = ImageGeneration.State.DOWNLOADED
        self.generation.save()
        return result

    def download_images(self) -> ReturnType:
        generator = ImageGeneratorFactory.create_generator()
        if generator is not None:
            # New backends deliver the finished image directly and are stored
            # in PassImagePrompt; there is nothing to download here.
            pass
        return self._download_midjourney_images()

    def _download_midjourney_images(self) -> ReturnType:
        """Download the Midjourney grid, split it and store the four images."""
        panel_name = os.path.basename(urlparse(self.generation.url).path)
        panel_image_path = os.path.join(self.temp_image_path, panel_name)

        if not download_midjourney_image(panel_image_path, url=self.generation.url):
            return Failure("download of midjourney image failed")

        quadrants = split_image_to_bytes(panel_image_path)
        if not quadrants:
            return Failure("splitting the midjourney image failed")

        images = [
            store_entity_image(data, self.entity, self.generation)
            for data in quadrants
        ]
        return Success(images)
