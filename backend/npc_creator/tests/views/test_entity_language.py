from django.test import TestCase
from rest_framework.test import APIClient

from npc_creator.models import Entity
from npc_creator.models.entities.npc import Npc


class EntityLanguageTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        for language in ("de", "en"):
            Npc.objects.create(
                state=Entity.States.PUBLISHED,
                language=language,
                attributes={"name": f"npc-{language}"},
            )

    def names(self, **params):
        response = self.client.get(
            "/api/npc_creator/entities/", {"kind[]": "Npc", **params}
        )
        return [e["values"]["name"] for e in response.json()["results"]]

    def test_list_only_shows_the_requested_language(self):
        self.assertEqual(self.names(lang="de"), ["npc-de"])
        self.assertEqual(self.names(lang="en"), ["npc-en"])

    def test_list_without_language_shows_all(self):
        self.assertCountEqual(self.names(), ["npc-de", "npc-en"])

    def test_default_language_is_german(self):
        self.assertEqual(Npc.objects.create().language, "de")
