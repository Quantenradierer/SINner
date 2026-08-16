from django.test import TestCase

from npc_creator.models.entity import Entity
from npc_creator.models.entities.location import Location


class TestLocation(TestCase):
    def test_location_creation_sets_kind_automatically(self):
        location = Location.objects.create(attributes={"name": "Test Location"})

        self.assertEqual(Entity.Kinds.LOCATION, location.kind)
        self.assertEqual({"name": "Test Location"}, location.attributes)
        self.assertIsNotNone(location.id)

    def test_location_defaults_to_unpublished(self):
        location = Location.objects.create()

        self.assertEqual(Entity.States.UNPUBLISHED, location.state)

    def test_location_manager_only_returns_locations(self):
        Location.objects.create()
        Entity.objects.create(kind=Entity.Kinds.NPC)

        self.assertEqual(1, Location.objects.count())
