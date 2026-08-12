"""
Tests for the Flexible Image Generation System
"""

import unittest
from unittest.mock import patch, MagicMock

from npc_creator.services.image_generation.dalle_image_generator import DalleImageGenerator
from npc_creator.services.image_generation.factory import ImageGeneratorFactory


class TestDalleImageGenerator(unittest.TestCase):
    
    @patch('npc_creator.services.image_generation.dalle_image_generator.OpenAI')
    def test_dalle_generator_creation(self, mock_openai):
        # Mock the OpenAI client properly
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        generator = DalleImageGenerator()
        self.assertIsInstance(generator, DalleImageGenerator)
        
    @patch('npc_creator.services.image_generation.dalle_image_generator.OpenAI')
    def test_dalle_generation_with_response(self, mock_openai):
        # Mock the API response
        mock_response = MagicMock()
        mock_data = MagicMock()
        mock_data.url = "https://example.com/image.jpg"
        mock_response.data = [mock_data]
        mock_openai.return_value.images.generate.return_value = mock_response
        
        generator = DalleImageGenerator()
        result = generator.generate_image("Test prompt")
        
        self.assertEqual(result, "https://example.com/image.jpg")


class TestImageGeneratorFactory(unittest.TestCase):
    
    def test_factory_returns_none_for_midjourney(self):
        # When no specific backend is set, it should return None (for legacy)
        with patch.dict('os.environ', {}, clear=True):
            generator = ImageGeneratorFactory.create_generator()
            self.assertIsNone(generator)
            
    @patch('os.getenv')
    def test_factory_dalle_backend(self, mock_getenv):
        mock_getenv.return_value = "dalle"
        generator = ImageGeneratorFactory.create_generator()
        # This will be None currently but in the future would return a DalleImageGenerator


if __name__ == '__main__':
    unittest.main()