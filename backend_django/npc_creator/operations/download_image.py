from typing import Optional

from npc_creator.operations.operation_output import Failure, Success
from npc_creator.repositories import npc_repo
from npc_creator import config
from npc_creator.services.midjourney.retrieve_latest_messages import retrieve_latest_messages
from npc_creator.services.midjourney.download_midjourney_image import download_midjourney_image
from npc_creator.services.midjourney.find_correlated_response import find_correlated_response
from npc_creator.services.midjourney.split_images import split_image


class DownloadImage:
    def __init__(self, npc, temp_image_path='data/midjourney/'):
        """
        Constructor of the GenerateImage class.

        Args:
            npc_id (int): The ID of the NPC for an image was created
        """
        self.npc = npc
        self.temp_image_path = temp_image_path

    def call(self) -> bool:
        """
        downloads and saves the image to the npc

        Returns:
            bool: True if the image was successfully saved, False otherwise.
        """
        if not self.npc.requires_image_download():
            return Failure('npc does not require an image download')

        result_image_paths = self.download_image()
        if result_image_paths:
            self.npc.add_image(result_image_paths.data[0])
        else:
            self.npc.image_generation_failed()

        npc_repo.save(self.npc)
        return result_image_paths

    def download_image(self) -> Optional[str]:
        responses = retrieve_latest_messages()
        url = find_correlated_response(responses, self.npc.image_generator_description)
        if not url:
            return Failure('could not find the correlated response or a OVERRIDE response')

        four_panel_image_path = download_midjourney_image(self.temp_image_path, url)
        if not four_panel_image_path:
            return Failure('download of midjourney image failed')

        images = split_image(four_panel_image_path, config.PUBLIC_NPC_IMAGE_PATH)
        if not images:
            return Failure('no image could be extracted')
        return Success(images)

