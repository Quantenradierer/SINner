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

from npc_creator.services.midjourney.find_correlated_response import (
    find_correlated_responses,
)
from npc_creator.services.midjourney.retrieve_latest_messages import (
    retrieve_latest_messages,
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

    @staticmethod
    def panel_exists(panel_name):
        return ImageGeneration.objects.filter(url=panel_name).exists()

    def add_images(self, image_paths):
        for name in image_paths:
            Image.objects.create(entity=self.entity, name=name, generation=self.generation)

    def download_images(self):
        responses = retrieve_latest_messages()
        urls = find_correlated_responses(responses, self.generation.id)

        for url in urls:
            panel_name = os.path.basename(urlparse(url).path)

            if not self.panel_exists(url):
                self.generation.url = url

                panel_image_path = os.path.join(self.temp_image_path, panel_name)
                success = download_midjourney_image(panel_image_path, url=url)
                if not success:
                    return Failure("download of midjourney image failed")

                image_names = split_image(
                    panel_image_path, self.images_names_iterator()
                )
                return Success(image_names)
        return Failure("could not find the correlated response or a OVERRIDE response")

    @staticmethod
    def images_names_iterator():
        while True:
            yield os.path.join(config.PUBLIC_ENTITY_IMAGE_PATH, str(uuid.uuid1()) + ".png")


if __name__ == "__main__":
    from npc_creator.operations.download_image import DownloadImage
    from npc_creator.models.image_generation import ImageGeneration

    objects = list(ImageGeneration.objects.all())
    print(DownloadImage(objects[-1]).call())
