import unittest

from django.test import TestCase
from django.contrib.auth import get_user_model

from npc_creator.models.collection import Collection
from npc_creator.models.entity import Entity
from npc_creator.models.favorite import Favorite

User = get_user_model()


class TestFavorite(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.collection = Collection.objects.create(
            name="Test Collection", user=self.user
        )
        self.entity = Entity.objects.create(
            kind="npc",
            data={"name": "Test NPC"},
            description="A test NPC",
        )

    def test_favorite_creation(self):
        """Test that a favorite can be created successfully."""
        favorite = Favorite.objects.create(
            entity=self.entity,
            collection=self.collection
        )
        
        self.assertEqual(favorite.entity, self.entity)
        self.assertEqual(favorite.collection, self.collection)
        self.assertIsNotNone(favorite.created_at)

    def test_unique_together_constraint(self):
        """Test that the unique_together constraint works correctly."""
        Favorite.objects.create(
            entity=self.entity,
            collection=self.collection
        )
        
        # This should raise an IntegrityError due to unique constraint
        with self.assertRaises(Exception):
            Favorite.objects.create(
                entity=self.entity,
                collection=self.collection
            )