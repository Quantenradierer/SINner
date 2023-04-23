from npc_creator.jobs import download_image
from npc_creator.operations.return_types import ReturnType, Success


class RecreateImage:
    def __init__(self, npc):
        """
        Constructor of the GenerateImage class.
        """

        self.npc = npc

    def call(self) -> ReturnType:
        """
        downloads and saves the image to the npc

        Returns:
            ReturnType: True if the image was successfully saved, False otherwise.
        """
        download_image.download_image_job_async(self.npc)
        return Success({})
