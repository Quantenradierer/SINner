import unittest
from unittest.mock import MagicMock

from services.midjourney.find_correlated_response import find_correlated_response, MIDJOURNEY_BOT_ID


class TestFindCorrelatedResponse(unittest.TestCase):

    def setUp(self):
        self.responses = [
            {
                'content': 'This is a response with no attachments',
                'author': {'id': '123'},
                'attachments': []
            },
            {
                'content': 'This is a response with an attachment that is not a PNG',
                'author': {'id': '456'},
                'attachments': [{'url': 'https://example.com/not_a_png.txt'}]
            },
            {
                'content': 'OVERRIDE This is a response with a PNG attachment',
                'author': {'id': '789'},
                'attachments': [{'url': 'https://example.com/image.png'}]
            },
            {
                'content': 'This is a response from the MIDJOURNEY_BOT with an search text and a PNG attachment',
                'author': {'id': MIDJOURNEY_BOT_ID},
                'attachments': [{'url': 'https://example.com/image.png'}]
            }
        ]

    def test_returns_correct_url(self):
        url = find_correlated_response(self.responses, 'with a PNG attachment')
        self.assertEqual('https://example.com/image.png', url)

    def test_returns_none_if_no_correlated_response(self):
        url = find_correlated_response(self.responses, 'not_found')
        self.assertIsNone(url)

    def test_ignores_responses_with_no_attachments(self):
        url = find_correlated_response(self.responses, 'no attachments')
        self.assertIsNone(url)

    def test_ignores_responses_with_non_png_attachments(self):
        url = find_correlated_response(self.responses, 'not_a_png')
        self.assertIsNone(url)

    def test_allows_override_search_text_for_non_MIDJOURNEY_BOT_responses(self):
        url = find_correlated_response(self.responses, 'override')
        self.assertIsNone(url)

    def test_allows_override_search_text_for_MIDJOURNEY_BOT_responses(self):
        responses = self.responses.copy()
        url = find_correlated_response(responses, 'This is a response with a PNG attachment')
        self.assertEqual('https://example.com/image.png', url)

    def test_handles_empty_responses_list(self):
        url = find_correlated_response([], 'image')
        self.assertIsNone(url)

    def test_handles_empty_search_text(self):
        url = find_correlated_response(self.responses, '')
        self.assertIsNone(url)

    def test_handles_missing_message_keys(self):
        responses = self.responses.copy()
        del responses[0]['content']
        url = find_correlated_response(responses, 'image')
        self.assertIsNone(url)
