import unittest

from npc_creator.services.image_generation.find_correlated_response import (
    MIDJOURNEY_BOT_ID,
    find_correlated_responses,
)


class TestFindCorrelatedResponses(unittest.TestCase):
    def setUp(self):
        self.seed = 111
        self.responses = [
            {
                "content": "This is a response with no attachments --seed 111",
                "author": {"id": "123"},
                "attachments": [],
            },
            {
                "content": "This is a response with a non-PNG attachment --seed 111",
                "author": {"id": MIDJOURNEY_BOT_ID},
                "attachments": [{"url": "https://example.com/not_a_png.txt"}],
            },
            {
                "content": "This is a response with the wrong seed --seed 222",
                "author": {"id": MIDJOURNEY_BOT_ID},
                "attachments": [{"url": "https://example.com/wrong_seed.png"}],
            },
            {
                "content": "This is a matching response --seed 111",
                "author": {"id": MIDJOURNEY_BOT_ID},
                "attachments": [{"url": "https://example.com/image.png"}],
            },
        ]

    def test_returns_matching_urls(self):
        urls = list(find_correlated_responses(self.responses, self.seed))
        self.assertEqual(["https://example.com/image.png"], urls)

    def test_returns_empty_if_no_seed_matches(self):
        urls = list(find_correlated_responses(self.responses, 999))
        self.assertEqual([], urls)

    def test_ignores_responses_with_no_attachments(self):
        responses = [self.responses[0]]
        urls = list(find_correlated_responses(responses, self.seed))
        self.assertEqual([], urls)

    def test_ignores_responses_with_non_png_attachments(self):
        responses = [self.responses[1]]
        urls = list(find_correlated_responses(responses, self.seed))
        self.assertEqual([], urls)

    def test_ignores_non_bot_responses_without_override(self):
        responses = [
            {
                "content": "This is a response with a matching seed --seed 111",
                "author": {"id": "someone-else"},
                "attachments": [{"url": "https://example.com/ignored.png"}],
            }
        ]
        urls = list(find_correlated_responses(responses, self.seed))
        self.assertEqual([], urls)

    def test_allows_override_for_non_bot_responses(self):
        responses = [
            {
                "content": "OVERRIDE This is a response with a matching seed --seed 111",
                "author": {"id": "someone-else"},
                "attachments": [{"url": "https://example.com/override.png"}],
            }
        ]
        urls = list(find_correlated_responses(responses, self.seed))
        self.assertEqual(["https://example.com/override.png"], urls)

    def test_handles_empty_responses_list(self):
        urls = list(find_correlated_responses([], self.seed))
        self.assertEqual([], urls)

    def test_handles_falsy_search_seed(self):
        urls = list(find_correlated_responses(self.responses, None))
        self.assertEqual([], urls)

    def test_handles_missing_message_keys(self):
        responses = [dict(self.responses[3])]
        del responses[0]["content"]
        urls = list(find_correlated_responses(responses, self.seed))
        self.assertEqual([], urls)
