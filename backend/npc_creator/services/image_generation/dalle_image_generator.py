import base64
import logging
import os
from typing import Optional

from constance import config
from openai import OpenAI

from npc_creator.services.image_generation.interface import ImageGeneratorInterface


class DalleImageGenerator(ImageGeneratorInterface):
    """Image generator using OpenAI's image generation model (configurable via DALLE_MODEL)."""

    def __init__(self):
        self.client = OpenAI()
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable is required")

        self.client.api_key = os.getenv("OPENAI_API_KEY")

    def generate_image(self, prompt: str) -> Optional[bytes]:
        """
        Generate an image using the configured OpenAI image model.

        Args:
            prompt (str): The prompt to use for image generation

        Returns:
            bytes: raw PNG image data, or None if failed
        """
        try:
            response = self.client.images.generate(
                model=config.DALLE_MODEL,
                prompt=prompt,
                size="1024x1024",
                n=1,
            )

            b64_data = response.data[0].b64_json
            if not b64_data:
                return None
            return base64.b64decode(b64_data)
        except Exception as e:
            logging.error(f"Error generating image with DALL-E: {e}")
            return None

    def is_available(self) -> bool:
        """
        Check if DALL-E generator is available.
        
        Returns:
            bool: True if API key is set and accessible, False otherwise
        """
        try:
            # Simple check by trying to access the client
            return bool(os.getenv("OPENAI_API_KEY"))
        except Exception:
            return False