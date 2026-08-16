"""
Tests for the Flexible Image Generation System
"""

import base64
import unittest
from unittest.mock import MagicMock, patch

from npc_creator.services.image_generation.dalle_image_generator import (
    DalleImageGenerator,
)
from npc_creator.services.image_generation.factory import ImageGeneratorFactory
from npc_creator.services.image_generation.gpt_vision_image_generator import (
    GptVisionImageGenerator,
)


class TestDalleImageGenerator(unittest.TestCase):
    @patch("npc_creator.services.image_generation.dalle_image_generator.OpenAI")
    def test_dalle_generator_creation(self, mock_openai):
        mock_openai.return_value = MagicMock()

        generator = DalleImageGenerator()
        self.assertIsInstance(generator, DalleImageGenerator)

    @patch("npc_creator.services.image_generation.dalle_image_generator.config")
    @patch("npc_creator.services.image_generation.dalle_image_generator.OpenAI")
    def test_dalle_generation_with_response(self, mock_openai, mock_config):
        mock_config.DALLE_MODEL = "gpt-image-1"
        image_bytes = b"fake-png-bytes"
        mock_data = MagicMock()
        mock_data.b64_json = base64.b64encode(image_bytes).decode()
        mock_response = MagicMock()
        mock_response.data = [mock_data]
        mock_openai.return_value.images.generate.return_value = mock_response

        generator = DalleImageGenerator()
        result = generator.generate_image("Test prompt")

        self.assertEqual(result, image_bytes)
        mock_openai.return_value.images.generate.assert_called_once_with(
            model="gpt-image-1", prompt="Test prompt", size="1024x1024", n=1
        )

    @patch("npc_creator.services.image_generation.dalle_image_generator.OpenAI")
    def test_dalle_generation_returns_none_on_error(self, mock_openai):
        mock_openai.return_value.images.generate.side_effect = Exception("API error")

        generator = DalleImageGenerator()
        result = generator.generate_image("Test prompt")

        self.assertIsNone(result)


class TestGptVisionImageGenerator(unittest.TestCase):
    @patch("npc_creator.services.image_generation.gpt_vision_image_generator.OpenAI")
    def test_generation_with_response(self, mock_openai):
        image_bytes = b"fake-png-bytes"
        image_call = MagicMock()
        image_call.type = "image_generation_call"
        image_call.result = base64.b64encode(image_bytes).decode()
        mock_response = MagicMock()
        mock_response.output = [image_call]
        mock_openai.return_value.responses.create.return_value = mock_response

        generator = GptVisionImageGenerator()
        result = generator.generate_image("Test prompt")

        self.assertEqual(result, image_bytes)

    @patch("npc_creator.services.image_generation.gpt_vision_image_generator.OpenAI")
    def test_generation_returns_none_without_image_call(self, mock_openai):
        message = MagicMock()
        message.type = "message"
        mock_response = MagicMock()
        mock_response.output = [message]
        mock_openai.return_value.responses.create.return_value = mock_response

        generator = GptVisionImageGenerator()
        result = generator.generate_image("Test prompt")

        self.assertIsNone(result)

    @patch("npc_creator.services.image_generation.gpt_vision_image_generator.OpenAI")
    def test_generation_returns_none_on_error(self, mock_openai):
        mock_openai.return_value.responses.create.side_effect = Exception("API error")

        generator = GptVisionImageGenerator()
        result = generator.generate_image("Test prompt")

        self.assertIsNone(result)


class TestImageGeneratorFactory(unittest.TestCase):
    def test_factory_returns_none_for_midjourney(self):
        with patch.dict("os.environ", {}, clear=True):
            generator = ImageGeneratorFactory.create_generator()
            self.assertIsNone(generator)

    def test_factory_dalle_backend(self):
        with patch.dict("os.environ", {"IMAGE_GENERATION_BACKEND": "dalle"}):
            generator = ImageGeneratorFactory.create_generator()
            self.assertIsInstance(generator, DalleImageGenerator)

    def test_factory_gpt_vision_backend(self):
        with patch.dict("os.environ", {"IMAGE_GENERATION_BACKEND": "gpt-vision"}):
            generator = ImageGeneratorFactory.create_generator()
            self.assertIsInstance(generator, GptVisionImageGenerator)
