import os.path
import uuid
from urllib.parse import urlparse

from npc_creator import config
from npc_creator.models.image import Image
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.return_types import Failure, Success, ReturnType
from npc_creator.services.image_generation.create_thumbnails import create_thumbnail
from npc_creator.services.image_generation.download_midjourney_image import (
    download_midjourney_image,
)

from npc_creator.services.image_generation.split_images import split_image


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

    @property
    def entity_directory(self):
        return os.path.join(config.PUBLIC_ENTITY_IMAGE_PATH, self.plural_entity_type())

    def download_images(self):
        panel_name = os.path.basename(urlparse(self.generation.url).path)

        panel_image_path = os.path.join(self.temp_image_path, panel_name)
        success = download_midjourney_image(panel_image_path, url=self.generation.url)
        if not success:
            return Failure("download of midjourney image failed")

        image_names = split_image(
            panel_image_path,
            self.images_names_iterator(),
        )
        for image_path in image_names:
            success = create_thumbnail(os.path.join(self.entity_directory, image_path))
            if not success:
                return Failure("thumbnail creation failed")
        return Success(image_names)

    def images_names_iterator(self) -> str:
        while True:
            yield os.path.join(self.entity_directory, str(uuid.uuid1()))
