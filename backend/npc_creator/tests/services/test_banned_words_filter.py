import unittest
from unittest.mock import mock_open, patch

from npc_creator.services.banned_words_filter import remove_banned_words


class TestContainsBannedWord(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_contains_banned_word(self, _mock_open):
        text = "This message contains the word porn"
        self.assertEqual("This message contains the word", remove_banned_words(text))

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_no_banned_word(self, _mock_open):
        text = "This message is free of any banned words"
        self.assertEqual(
            "This message is free of any banned words", remove_banned_words(text)
        )

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_banned_word_in_sentence(self, _mock_open):
        text = "This message contains the word porn. However, there is a dot behind it."
        self.assertEqual(
            "This message contains the word . However, there is a dot behind it.",
            remove_banned_words(text),
        )

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_banned_word_in_quotes(self, _mock_open):
        text = "This message contains the word 'porn'."
        self.assertEqual(
            "This message contains the word ''.", remove_banned_words(text)
        )

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_contains_banned_words_with_space(self, _mock_open):
        text = "This message contains the word porn and some other unrelated words."
        self.assertEqual(
            "This message contains the word  and some other unrelated words.",
            remove_banned_words(text),
        )

    @patch("builtins.open", new_callable=mock_open, read_data="Porn\ntied up\npetite\n")
    def test_contains_case_sensitive_banned_words(self, _mock_open):
        text = "This message contains the word porn and some other unrelated words."
        self.assertEqual(
            "This message contains the word  and some other unrelated words.",
            remove_banned_words(text),
        )

    @patch("builtins.open", new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_contains_case_sensitive_text(self, _mock_open):
        text = "This message contains the word Porn and some other unrelated words."
        self.assertEqual(
            "This message contains the word  and some other unrelated words.",
            remove_banned_words(text),
        )
