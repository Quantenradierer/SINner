import unittest

from django.test import TestCase

from npc_creator.models.entities.location import Location


class TestLocation(TestCase):
    def test_location_creation(self):
        """Test that a location can be created successfully."""
        location_data = {
            "name": "Test Location",
            "description": "A test location description",
            "type": "building",
            "data": {
                "address": "123 Test Street",
                "size": "medium"
            }
        }
        
        location = Location.objects.create(**location_data)
        
        self.assertEqual(location.name, "Test Location")
        self.assertEqual(location.description, "A test location description")
        self.assertEqual(location.type, "building")
        self.assertEqual(location.data["address"], "123 Test Street")
        self.assertEqual(location.data["size"], "medium")
        self.assertIsNotNone(location.id)

    def test_location_str_representation(self):
        """Test that the string representation is correct."""
        location_data = {
            "name": "Test Location",
            "description": "A test location description",
            "type": "building",
            "data": {}
        }
        
        location = Location.objects.create(**location_data)
        expected_str = f"Location: {location.name}"
        self.assertEqual(str(location), expected_str)