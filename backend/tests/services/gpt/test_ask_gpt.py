import unittest
from unittest.mock import patch

from services.gpt.ask_gpt import ask_gpt


class TestAskGpt(unittest.TestCase):
    @patch('openai.Completion.create')
    def test_success(self, mock_create):
        mock_create.return_value = {
            "choices": [{"text": "This is the GPT response."}]
        }
        prompt = "This is the GPT prompt."
        expected = "This is the GPT response."
        actual = ask_gpt(prompt)
        self.assertEqual(actual, expected)