
from npc_creator.operations.generate_npc import GenerateNpc
from npc_creator.operations.return_types import  ReturnType


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
        self.npc.reset_image()
        return GenerateNpc(npc=self.npc).call()
