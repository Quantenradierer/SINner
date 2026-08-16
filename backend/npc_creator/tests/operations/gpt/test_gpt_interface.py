import unittest
from unittest.mock import patch

from npc_creator.operations.gpt.gpt_interface import GptInterface


class TestGptInterfaceModelSelection(unittest.TestCase):
    @patch("npc_creator.operations.gpt.gpt_interface.config")
    def test_uses_configured_model_when_valid(self, mock_config):
        mock_config.DEFAULT_GPT_MODEL = "gpt-4.1-mini"

        interface = GptInterface()

        self.assertEqual(GptInterface.GptVersion.GPT4_1_Mini, interface.gpt)

    @patch("npc_creator.operations.gpt.gpt_interface.config")
    def test_falls_back_to_default_for_unknown_model(self, mock_config):
        mock_config.DEFAULT_GPT_MODEL = "not-a-real-model"

        interface = GptInterface()

        self.assertEqual(GptInterface.GptVersion.GPT4_O_Mini, interface.gpt)
