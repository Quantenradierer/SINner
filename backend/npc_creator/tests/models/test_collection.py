import unittest

from django.test import TestCase
from django.contrib.auth import get_user_model

from npc_creator.models.collection import Collection

User = get_user_model()


class TestCollection(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.collection_data = {
            "name": "Test Collection",
            "user": self.user,
        }

    def test_collection_creation(self):
        """Test that a collection can be created successfully."""
        collection = Collection.objects.create(**self.collection_data)
        
        self.assertEqual(collection.name, "Test Collection")
        self.assertEqual(collection.user, self.user)
        self.assertIsNotNone(collection.id)

    def test_collection_str_representation(self):
        """Test that the string representation is correct."""
        collection = Collection.objects.create(**self.collection_data)
        expected_str = f"Collection: {collection.name}"
        self.assertEqual(str(collection), expected_str)

    def test_unique_together_constraint(self):
        """Test that the unique_together constraint works correctly."""
        Collection.objects.create(**self.collection_data)
        
        # This should raise an IntegrityError due to unique constraint
        with self.assertRaises(Exception):
            Collection.objects.create(**self.collection_data)