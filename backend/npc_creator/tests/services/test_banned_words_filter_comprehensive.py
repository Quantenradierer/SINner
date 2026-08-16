import unittest
from unittest.mock import mock_open, patch

from npc_creator.services.banned_words_filter import (
    banned_words_regex,
    remove_banned_words,
)


class TestBannedWordsFilterComprehensive(unittest.TestCase):
    def setUp(self):
        banned_words_regex.cache_clear()

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_basic(self, _mock_open):
        """Test basic banned words removal."""
        text = "This message contains the word porn"
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_no_match(self, _mock_open):
        """Test text without banned words remains unchanged."""
        text = "This message is free of any banned words"
        result = remove_banned_words(text)
        self.assertEqual(result, "This message is free of any banned words")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_multiple_matches(self, _mock_open):
        """Test removal of multiple banned words."""
        text = "This message contains the word porn and some other tied up words."
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word and some other words.")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_sentence_end(self, _mock_open):
        """Test banned words at sentence end."""
        text = "This message contains the word porn. However, there is a dot behind it."
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word . However, there is a dot behind it.")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_in_quotes(self, _mock_open):
        """Test banned words in quotes."""
        text = "This message contains the word 'porn'."
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word ''.")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_with_space(self, _mock_open):
        """Test banned words with spaces."""
        text = "This message contains the word porn and some other unrelated words."
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word and some other unrelated words.")

    @patch("builtins.open", new_callable=mock_open, read_data="Porn\ntied up\npetite\n")
    def test_remove_banned_words_case_insensitive(self, _mock_open):
        """Test case insensitive matching."""
        text = "This message contains the word porn and some other unrelated words."
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word and some other unrelated words.")

    @patch("builtins.open", new_callable=mock_open, read_data="Porn\ntied up\npetite\n")
    def test_remove_banned_words_case_sensitive_text(self, _mock_open):
        """Test case sensitive text handling."""
        text = "This message contains the word Porn and some other unrelated words."
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word and some other unrelated words.")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_remove_banned_words_empty_list(self, _mock_open):
        """Test with empty banned words list."""
        text = "This message contains the word porn"
        result = remove_banned_words(text)
        self.assertEqual(result, "This message contains the word porn")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_empty_text(self, _mock_open):
        """Test with empty text."""
        text = ""
        result = remove_banned_words(text)
        self.assertEqual(result, "")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_whitespace_only(self, _mock_open):
        """Test with whitespace only."""
        text = "   "
        result = remove_banned_words(text)
        self.assertEqual(result, "")

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_remove_banned_words_only_banned_words(self, _mock_open):
        """Test with only banned words."""
        text = "porn tied up petite"
        result = remove_banned_words(text)
        self.assertEqual(result, "")