import base64
import logging
import os
from typing import Optional

from openai import OpenAI

from npc_creator.services.image_generation.interface import ImageGeneratorInterface


class GptVisionImageGenerator(ImageGeneratorInterface):
    """Image generator using OpenAI's chat-based image generation tool."""

    MODEL = "gpt-4.1-mini"

    def __init__(self):
        self.client = OpenAI()
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable is required")

        self.client.api_key = os.getenv("OPENAI_API_KEY")

    def generate_image(self, prompt: str) -> Optional[bytes]:
        """
        Generate an image via a chat completion using the image_generation tool.

        Args:
            prompt (str): The prompt to use for image generation

        Returns:
            bytes: raw PNG image data, or None if failed
        """
        try:
            response = self.client.responses.create(
                model=self.MODEL,
                input=f"Generate an image: {prompt}",
                tools=[{"type": "image_generation"}],
            )

            image_calls = [
                output
                for output in response.output
                if output.type == "image_generation_call"
            ]
            if not image_calls or not image_calls[0].result:
                return None

            return base64.b64decode(image_calls[0].result)
        except Exception as e:
            logging.error(f"Error generating image with GPT image tool: {e}")
            return None

    def is_available(self) -> bool:
        """
        Check if GPT-4V generator is available.
        
        Returns:
            bool: True if API key is set and accessible, False otherwise
        """
        try:
            # Simple check by trying to access the client
            return bool(os.getenv("OPENAI_API_KEY"))
        except Exception:
            return False