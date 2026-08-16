import unittest
from unittest.mock import Mock, patch

from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.gpt.entity.pass_image_prompt import PassImagePrompt
from npc_creator.operations.return_types import Failure, Success


class ConcretePassImagePrompt(PassImagePrompt):
    """special_midjourney_prompt is abstract on the base class; give it a
    trivial implementation so the Midjourney fallback path can be tested."""

    def special_midjourney_prompt(self, prompt):
        return "some-template", prompt


def make_generation(description=""):
    generation = Mock(spec=ImageGeneration)
    generation.description = description
    generation.entity = Mock()
    generation.entity.image_generator_description = "someone with glasses"
    return generation


class TestPassImagePromptWithFactoryBackend(unittest.TestCase):
    @patch("npc_creator.operations.gpt.entity.pass_image_prompt.ImageGeneratorFactory")
    def test_call_success_sets_url_and_state(self, mock_factory):
        generator = Mock()
        generator.generate_image.return_value = "https://example.com/image.png"
        mock_factory.create_generator.return_value = generator

        generation = make_generation(description="a description")

        result = PassImagePrompt(generation).call()

        self.assertTrue(result)
        self.assertEqual("https://example.com/image.png", generation.url)
        self.assertEqual(ImageGeneration.State.IN_PROGRESS, generation.state)
        generation.save.assert_called_once()

    @patch("npc_creator.operations.gpt.entity.pass_image_prompt.ImageGeneratorFactory")
    def test_call_failure_when_generator_returns_no_url(self, mock_factory):
        generator = Mock()
        generator.generate_image.return_value = None
        mock_factory.create_generator.return_value = generator

        generation = make_generation(description="a description")

        result = PassImagePrompt(generation).call()

        self.assertFalse(result)
        self.assertEqual("image_generation_failed", result.error)

    @patch("npc_creator.operations.gpt.entity.pass_image_prompt.ImageGeneratorFactory")
    def test_generates_description_when_missing(self, mock_factory):
        generator = Mock()
        generator.generate_image.return_value = "https://example.com/image.png"
        mock_factory.create_generator.return_value = generator

        generation = make_generation(description="")
        translate_result = Success("a generated description")
        generation.entity.instance.Translate.return_value.call.return_value = (
            translate_result
        )

        PassImagePrompt(generation).call()

        generation.entity.instance.Translate.assert_called_once_with(
            entity=generation.entity
        )
        self.assertEqual("a generated description", generation.description)

    @patch("npc_creator.operations.gpt.entity.pass_image_prompt.ImageGeneratorFactory")
    def test_skips_description_generation_when_already_present(self, mock_factory):
        generator = Mock()
        generator.generate_image.return_value = "https://example.com/image.png"
        mock_factory.create_generator.return_value = generator

        generation = make_generation(description="already there")

        PassImagePrompt(generation).call()

        generation.entity.instance.Translate.assert_not_called()


class TestPassImagePromptMidjourneyFallback(unittest.TestCase):
    @patch("npc_creator.operations.gpt.entity.pass_image_prompt.ImageGeneratorFactory")
    def test_no_generator_falls_back_to_midjourney(self, mock_factory):
        mock_factory.create_generator.return_value = None

        generation = make_generation(description="a description")

        with patch(
            "npc_creator.services.image_generation.pass_prompt.pass_prompt",
            return_value=True,
        ):
            result = ConcretePassImagePrompt(generation).call()

        self.assertTrue(result)
        self.assertEqual("some-template", generation.template)
        self.assertEqual(ImageGeneration.State.IN_PROGRESS, generation.state)

    @patch("npc_creator.operations.gpt.entity.pass_image_prompt.ImageGeneratorFactory")
    def test_midjourney_send_failure_returns_failure(self, mock_factory):
        mock_factory.create_generator.return_value = None

        generation = make_generation(description="a description")

        with patch(
            "npc_creator.services.image_generation.pass_prompt.pass_prompt",
            return_value=False,
        ):
            result = ConcretePassImagePrompt(generation).call()

        self.assertFalse(result)
        self.assertEqual("sending_midjourney_prompt_was_unsuccessful", result.error)

    def test_base_class_requires_subclass_implementation(self):
        generation = make_generation(description="a description")

        with self.assertRaises(NotImplementedError):
            PassImagePrompt(generation).special_midjourney_prompt("a prompt")
