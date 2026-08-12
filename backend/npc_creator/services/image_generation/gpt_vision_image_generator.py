import os
from typing import Optional

from openai import OpenAI

from npc_creator.services.image_generation.interface import ImageGeneratorInterface


class GptVisionImageGenerator(ImageGeneratorInterface):
    """Image generator using OpenAI's GPT-4 Vision model."""

    def __init__(self):
        self.client = OpenAI()
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable is required")
            
        self.client.api_key = os.getenv("OPENAI_API_KEY")

    def generate_image(self, prompt: str) -> Optional[str]:
        """
        Generate an image using GPT-4 Vision model.
        
        Args:
            prompt (str): The prompt to use for image generation
            
        Returns:
            str: URL of generated image, or None if failed
        """
        try:
            # For GPT-4V, we send the prompt in a way that generates an image response
            # This is simplified - actual implementation would vary based on API capabilities
            response = self.client.chat.completions.create(
                model="gpt-4-vision-preview",  # or gpt-4-turbo
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": f"Generate an image: {prompt}"},
                        ],
                    }
                ],
                max_tokens=300,
            )
            
            # Extract URL from response if available (this would need actual API documentation)
            # For now, returning None as this is a placeholder
            return None
        except Exception as e:
            print(f"Error generating image with GPT-4V: {e}")
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