import unittest
from unittest.mock import patch

from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt


class TestAskChatgpt(unittest.TestCase):
    @patch("openai.ChatCompletion.create")
    def test_ask_chatgpt(self, mock_create):
        mock_create.return_value = {
            "choices": [{"message": {"content": "This is the Chat GPT response."}}]
        }
        prompts = ["This is the Chat GPT prompt."]
        expected = "This is the Chat GPT response."
        actual = ask_chatgpt("", prompts)
        self.assertEqual(actual, expected)

    @patch("openai.ChatCompletion.create", side_effect=Exception("Test Error"))
    def test_ask_chatgpt_error(self, _mock_create):
        prompts = "This is the Chat GPT prompt."
        expected = None
        actual = ask_chatgpt("", prompts)
        self.assertEqual(actual, expected)
