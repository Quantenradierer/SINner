import os


class ImageGenerationConfig:
    """Configuration class for image generation settings."""
    
    @staticmethod
    def get_backend() -> str:
        """
        Get the configured image generation backend.
        
        Returns:
            str: The selected backend ("midjourney", "dalle", or "gpt-vision")
        """
        return os.getenv("IMAGE_GENERATION_BACKEND", "midjourney").lower()
    
    @staticmethod
    def is_dalle_enabled() -> bool:
        """Check if DALL-E is the selected backend."""
        return ImageGenerationConfig.get_backend() == "dalle"
    
    @staticmethod
    def is_gpt_vision_enabled() -> bool:
        """Check if GPT-4V is the selected backend."""
        return ImageGenerationConfig.get_backend() == "gpt-vision"
    
    @staticmethod
    def is_midjourney_enabled() -> bool:
        """Check if Midjourney is the selected backend (default)."""
        return ImageGenerationConfig.get_backend() == "midjourney"