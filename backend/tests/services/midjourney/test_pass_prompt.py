
import unittest
from unittest.mock import patch

from services.midjourney.pass_prompt import pass_prompt


class TestPassPrompt(unittest.TestCase):
    @patch('requests.post')
    def test_successful_request(self, mock_post):
        mock_post.return_value.status_code = 200

        result = pass_prompt('Test prompt')

        self.assertTrue(result)
        mock_post.assert_called_once()

    @patch('requests.post')
    def test_unauthorized_request(self, mock_post):
        mock_post.return_value.status_code = 401

        result = pass_prompt('Test prompt')

        self.assertFalse(result)
        mock_post.assert_called_once()
