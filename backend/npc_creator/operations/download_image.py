import os.path

from npc_creator import config
from npc_creator.models import Npc
from npc_creator.models.panel_image import PanelImage
from npc_creator.operations.return_types import Failure, Success, ReturnType
from npc_creator.repositories import npc_repo, panel_image_repo
from npc_creator.services.midjourney.download_midjourney_image import download_midjourney_image

from npc_creator.services.midjourney.find_correlated_response import find_correlated_responses
from npc_creator.services.midjourney.retrieve_latest_messages import retrieve_latest_messages
from npc_creator.services.midjourney.split_images import split_image


class DownloadImage:
    def __init__(self, npc: Npc, temp_image_path='data/midjourney/'):
        """
        Constructor of the GenerateImage class.
        """

        self.npc = npc
        self.temp_image_path = temp_image_path

    def call(self) -> ReturnType:
        """
        downloads and saves the image to the npc

        Returns:
            ReturnType: True if the image was successfully saved, False otherwise.
        """
        result_image_paths = self.download_images()
        self.npc.refresh_from_db()
        if result_image_paths:
            self.npc.add_images(len(result_image_paths.data))
        else:
            self.npc.image_generation_failed()


        npc_repo.save(self.npc)
        return result_image_paths

    def download_images(self):
        responses = retrieve_latest_messages()
        urls = find_correlated_responses(responses, self.npc.image_generator_description)
        image_paths_iter = self.images_names_iterator(self.npc.image_url, self.npc.id)

        for url in urls:
            panel_name = os.path.basename(url)

            if not panel_image_repo.exists(panel_name):
                panel_image = PanelImage(panel_name=panel_name, description=self.npc.image_generator_description)
                panel_image_repo.save(panel_image)

                panel_image_path = os.path.join(self.temp_image_path, panel_name)
                success = download_midjourney_image(panel_image_path, url=url)
                if not success:
                    return Failure('download of midjourney image failed')

                image_names = split_image(panel_image_path, image_paths_iter)
                return Success(image_names)
        return Failure('could not find the correlated response or a OVERRIDE response')

    @staticmethod
    def images_names_iterator(image_url, pk):
        counter = 1
        while True:
            path = os.path.join(config.PUBLIC_NPC_IMAGE_PATH, image_url.format(pk=pk, counter=counter))

            if not os.path.isfile(path):
                yield path
            counter += 1
