import os
from typing import Optional

from npc_creator.services.image_generation.dalle_image_generator import DalleImageGenerator
from npc_creator.services.image_generation.gpt_vision_image_generator import GptVisionImageGenerator
from npc_creator.services.image_generation.interface import ImageGeneratorInterface


class ImageGeneratorFactory:
    """Factory for creating image generators based on configuration."""

    @staticmethod
    def create_generator() -> Optional[ImageGeneratorInterface]:
        """
        Create an image generator based on configuration.
        
        Returns:
            ImageGeneratorInterface: An instance of an image generator,
            or None if no valid generator can be created.
        """
        # For now, we'll maintain backward compatibility and return None
        # to let the system fall back to existing Midjourney behavior in pass_image_prompt
        
        # We're using a simple approach for now - direct detection from environment variable
        backend = os.getenv("IMAGE_GENERATION_BACKEND", "midjourney").lower()
        
        if backend == "dalle":
            try:
                return DalleImageGenerator()
            except Exception as e:
                print(f"Failed to create DALL-E generator: {e}")
                return None
        elif backend == "gpt-vision":
            try:
                return GptVisionImageGenerator() 
            except Exception as e:
                print(f"Failed to create GPT-4V generator: {e}")
                return None
        # Default to midjourney (maintaining backward compatibility)  
        else:
            # For legacy support, we return None so original pass_prompt logic is used
            return None

    @staticmethod
    def is_available() -> bool:
        """
        Check if selected image generator is available.
        
        Returns:
            bool: True if the selected generator is available, False otherwise
        """
        return False  # For now, always fall back to old behavior

    @staticmethod
    def get_available_backends() -> list:
        """
        Get list of available backends based on current setup.
        
        Returns:
            list: List of available backend names
        """
        return ["midjourney", "dalle", "gpt-vision"]

    @staticmethod
    def get_current_backend_config() -> dict:
        """
        Get configuration for the currently selected backend.
        
        Returns:
            dict: Configuration for the current backend
        """
        config_map = {
            "midjourney": {
                "name": "Midjourney",
                "description": "Legacy Midjourney integration",
                "enabled": True,
                "requires_api_key": False
            },
            "dalle": {
                "name": "DALL-E", 
                "description": "OpenAI DALL-E image generation",
                "enabled": bool(os.getenv("OPENAI_API_KEY")),
                "requires_api_key": True
            },
            "gpt-vision": {
                "name": "GPT-Vision",
                "description": "OpenAI GPT-4 Vision integration",  
                "enabled": bool(os.getenv("OPENAI_API_KEY")),
                "requires_api_key": True
            }
        }
        
        backend = os.getenv("IMAGE_GENERATION_BACKEND", "midjourney").lower()
        return config_map.get(backend, config_map["midjourney"])