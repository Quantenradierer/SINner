from abc import ABC, abstractmethod
from typing import Optional


class ImageGeneratorInterface(ABC):
    """Abstract base class for all image generation implementations."""

    @abstractmethod
    def generate_image(self, prompt: str) -> Optional[bytes]:
        """
        Generate an image from a prompt.

        Args:
            prompt (str): The prompt to use for image generation

        Returns:
            bytes: raw image data (PNG), or None if failed
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """
        Check if this image generator is available/accessible.
        
        Returns:
            bool: True if the generator can be used, False otherwise
        """
        pass