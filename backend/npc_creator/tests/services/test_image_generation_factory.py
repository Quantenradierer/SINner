import unittest
from unittest.mock import patch, MagicMock

from django.test import TestCase

from npc_creator.services.image_generation.factory import ImageGeneratorFactory


class TestImageGeneratorFactory(TestCase):
    @patch("npc_creator.services.image_generation.factory.os.getenv")
    def test_create_generator_default_midjourney(self, mock_getenv):
        """Test that factory defaults to midjourney when no env var set."""
        mock_getenv.side_effect = lambda key, default=None: default
        
        generator = ImageGeneratorFactory.create_generator()
        # Should return None for backward compatibility
        self.assertIsNone(generator)

    @patch("npc_creator.services.image_generation.factory.os.getenv")
    def test_create_generator_dalle(self, mock_getenv):
        """Test that factory creates DALL-E generator when specified."""
        mock_getenv.side_effect = lambda key, default=None: "dalle" if key == "IMAGE_GENERATION_BACKEND" else default
        
        # Mock the import and class creation to avoid dependency issues
        with patch("npc_creator.services.image_generation.factory.DalleImageGenerator") as mock_dalle:
            mock_instance = MagicMock()
            mock_dalle.return_value = mock_instance
            
            generator = ImageGeneratorFactory.create_generator()
            
            # Should return a DALL-E instance when properly configured
            self.assertIsNotNone(generator)

    @patch("npc_creator.services.image_generation.factory.os.getenv")
    def test_create_generator_gpt_vision(self, mock_getenv):
        """Test that factory creates GPT-4V generator when specified."""
        mock_getenv.side_effect = lambda key, default=None: "gpt-vision" if key == "IMAGE_GENERATION_BACKEND" else default
        
        # Mock the import and class creation to avoid dependency issues
        with patch("npc_creator.services.image_generation.factory.GptVisionImageGenerator") as mock_gpt_vision:
            mock_instance = MagicMock()
            mock_gpt_vision.return_value = mock_instance
            
            generator = ImageGeneratorFactory.create_generator()
            
            # Should return a GPT-4V instance when properly configured
            self.assertIsNotNone(generator)

    def test_is_available(self):
        """Test that is_available always returns False for now."""
        result = ImageGeneratorFactory.is_available()
        self.assertFalse(result)

    def test_get_available_backends(self):
        """Test that available backends are correctly reported."""
        backends = ImageGeneratorFactory.get_available_backends()
        expected = ["midjourney", "dalle", "gpt-vision"]
        self.assertEqual(backends, expected)

    @patch("npc_creator.services.image_generation.factory.os.getenv")
    def test_get_current_backend_config_default(self, mock_getenv):
        """Test that default backend configuration is returned."""
        mock_getenv.side_effect = lambda key, default=None: default
        
        config = ImageGeneratorFactory.get_current_backend_config()
        # Should default to midjourney config
        self.assertEqual(config["name"], "Midjourney")
        self.assertTrue(config["enabled"])

    @patch("npc_creator.services.image_generation.factory.os.getenv")
    def test_get_current_backend_config_dalle(self, mock_getenv):
        """Test that DALL-E backend configuration is correctly returned."""
        mock_getenv.side_effect = lambda key, default=None: "dalle" if key == "IMAGE_GENERATION_BACKEND" else default
        
        config = ImageGeneratorFactory.get_current_backend_config()
        # Should return DALL-E config
        self.assertEqual(config["name"], "DALL-E")
        self.assertTrue(config["requires_api_key"])