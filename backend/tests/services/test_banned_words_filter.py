import unittest
from unittest.mock import mock_open, patch

from services.banned_words_filter import contains_banned_word, banned_words


class TestContainsBannedWord(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_contains_banned_word(self, mock_open):
        text = "This message contains the word porn"
        self.assertTrue(contains_banned_word(text))

        text = "This message is free of any banned words"
        self.assertFalse(contains_banned_word(text))

    @patch('builtins.open', new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_banned_words(self, mock_file):
        expected = [' porn ', ' tied up ', ' petite ']
        actual = banned_words()
        self.assertEqual(actual, expected)