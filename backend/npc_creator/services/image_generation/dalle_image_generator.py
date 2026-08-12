import os
from typing import Optional

from openai import OpenAI

from npc_creator.services.image_generation.interface import ImageGeneratorInterface


class DalleImageGenerator(ImageGeneratorInterface):
    """Image generator using OpenAI's DALL-E model."""

    def __init__(self):
        self.client = OpenAI()
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable is required")
            
        self.client.api_key = os.getenv("OPENAI_API_KEY")

    def generate_image(self, prompt: str) -> Optional[str]:
        """
        Generate an image using DALL-E.
        
        Args:
            prompt (str): The prompt to use for image generation
            
        Returns:
            str: URL of generated image, or None if failed
        """
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            return response.data[0].url
        except Exception as e:
            # Log the error properly in a real implementation
            print(f"Error generating image with DALL-E: {e}")
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