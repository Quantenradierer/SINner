import json
import unittest
from unittest.mock import Mock, patch

from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated


def make_completion(content):
    completion = Mock()
    completion.choices = [Mock(message=Mock(content=content))]
    return completion


class TestAskChatgptModerated(unittest.TestCase):
    @patch("npc_creator.services.gpt.ask_chatgpt.client")
    def test_ask_chatgpt_moderated_success(self, mock_client):
        mock_client.chat.completions.create.return_value = make_completion(
            "This is the Chat GPT response."
        )

        result = ask_chatgpt_moderated("system prompt", ["user prompt"], "gpt-4o-mini")

        self.assertTrue(result)
        self.assertEqual(result.data, "This is the Chat GPT response.")

    @patch("npc_creator.services.gpt.ask_chatgpt.client")
    def test_ask_chatgpt_moderated_json(self, mock_client):
        mock_client.chat.completions.create.return_value = make_completion(
            json.dumps({"key": "value"})
        )

        result = ask_chatgpt_moderated(
            "system prompt", ["user prompt"], "gpt-4o-mini", use_json=True
        )

        self.assertTrue(result)
        self.assertEqual(result.data, {"key": "value"})

    @patch("npc_creator.services.gpt.ask_chatgpt.client")
    def test_ask_chatgpt_moderated_error(self, mock_client):
        mock_client.chat.completions.create.side_effect = Exception("Test Error")

        result = ask_chatgpt_moderated("system prompt", ["user prompt"], "gpt-4o-mini")

        self.assertFalse(result)
        self.assertEqual(result.error, "gpt_raised_an_error")
