import unittest
from unittest.mock import patch

from npc_creator.services.interpret_gpt import find_correct_key, dict_from_text


class TestInterpretGpt(unittest.TestCase):
    def test_find_correct_key_exact_match(self):
        """Test that exact key matches are returned correctly."""
        used_attribute_keys = ["Name", "Age", "Strength"]
        key = "Name"
        
        result = find_correct_key(used_attribute_keys, key)
        self.assertEqual(result, "Name")

    def test_find_correct_key_partial_match(self):
        """Test partial matching logic works correctly."""
        used_attribute_keys = ["Glück (1-6)", "Stärke", "Wille"]
        key = "Glück"
        
        result = find_correct_key(used_attribute_keys, key)
        self.assertEqual(result, "Glück (1-6)")

    def test_find_correct_key_no_match_returns_original(self):
        """Test that when no match is found, the original key is returned."""
        used_attribute_keys = ["Name", "Age", "Strength"]
        key = "NonExistent"
        
        result = find_correct_key(used_attribute_keys, key)
        self.assertEqual(result, "NonExistent")

    def test_dict_from_text_basic(self):
        """Test basic dictionary creation from text."""
        used_attribute_keys = ["Name", "Age", "Strength"]
        text = "Name: John\nAge: 30\nStrength: 15"
        
        result = dict_from_text(used_attribute_keys, text)
        expected = {"Name": "John", "Age": "30", "Strength": "15"}
        self.assertEqual(result, expected)

    def test_dict_from_text_with_partial_match(self):
        """Test dictionary creation with partial key matching."""
        used_attribute_keys = ["Glück (1-6)", "Stärke", "Wille"]
        text = "Glück: 12\nStärke: 8\nWille: 10"
        
        result = dict_from_text(used_attribute_keys, text)
        expected = {"Glück (1-6)": "12", "Stärke": "8", "Wille": "10"}
        self.assertEqual(result, expected)

    def test_dict_from_text_ignores_non_keys(self):
        """Test that lines without colons are ignored."""
        used_attribute_keys = ["Name", "Age"]
        text = "Name: John\nThis is a comment\nAge: 30"
        
        result = dict_from_text(used_attribute_keys, text)
        expected = {"Name": "John", "Age": "30"}
        self.assertEqual(result, expected)

    def test_dict_from_text_no_match_ignored(self):
        """Test that keys not in used_attribute_keys are ignored."""
        used_attribute_keys = ["Name", "Age"]
        text = "Name: John\nHeight: 180\nAge: 30"
        
        result = dict_from_text(used_attribute_keys, text)
        expected = {"Name": "John", "Age": "30"}
        self.assertEqual(result, expected)

    def test_dict_from_text_empty_text(self):
        """Test empty text handling."""
        used_attribute_keys = ["Name", "Age"]
        text = ""
        
        result = dict_from_text(used_attribute_keys, text)
        self.assertEqual(result, {})

    def test_dict_from_text_line_without_colon(self):
        """Test that lines without colons are ignored."""
        used_attribute_keys = ["Name", "Age"]
        text = "Name: John\nSome random line\nAge: 30\nAnother random line"
        
        result = dict_from_text(used_attribute_keys, text)
        expected = {"Name": "John", "Age": "30"}
        self.assertEqual(result, expected)