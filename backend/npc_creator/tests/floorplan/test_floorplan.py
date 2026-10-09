import json
import shutil
import tempfile
from importlib.util import find_spec
from unittest import skipUnless
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from rest_framework.test import APIClient

from npc_creator.jobs.floorplan_job import floorplan_job
from npc_creator.models import Entity
from npc_creator.models.entities.floorplan import Floorplan
from npc_creator.models.floorplan import FloorplanFile, FloorplanGeneration
from npc_creator.services.floorplan.request import RequestError, parse_request

PARAMS = {
    "building_type": "office",
    "width": 30,
    "depth": 20,
    "floors_above": 2,
    "seed": 1,
}


@skipUnless(find_spec("roomplanner"), "roomplanner is not installed")
class TestParseRequest(TestCase):
    def test_pins_a_random_seed(self):
        request = parse_request({"params": {**PARAMS, "seed": None}})

        self.assertIsInstance(request.params.seed, int)

    def test_defaults(self):
        request = parse_request({"params": PARAMS})

        self.assertEqual("neon2", request.theme)
        self.assertEqual("de", request.language)

    def test_language_is_kept_and_stored(self):
        request = parse_request({"params": PARAMS, "language": "en"})

        self.assertEqual("en", request.language)
        self.assertEqual("en", request.as_attributes()["language"])

    def test_rejects_what_exceeds_a_cap(self):
        for change in (
            {"width": 500},
            {"depth": 2},
            {"floors_above": 50},
            {"floors_below": 9},
            {"seed": -1},
        ):
            with self.subTest(change), self.assertRaises(RequestError):
                parse_request({"params": {**PARAMS, **change}})

    def test_rejects_bad_options(self):
        for extra in ({"theme": "neon"}, {"language": "fr"}):
            with self.subTest(extra), self.assertRaises(RequestError):
                parse_request({"params": PARAMS, **extra})

    def test_rejects_unknown_params(self):
        with self.assertRaises(RequestError):
            parse_request({"params": {**PARAMS, "bogus": 1}})

    def test_rejects_non_objects(self):
        for data in (None, [], {"params": "x"}):
            with self.subTest(data), self.assertRaises(RequestError):
                parse_request(data)


@skipUnless(find_spec("roomplanner"), "roomplanner is not installed")
class TestFloorplanApi(TestCase):
    def setUp(self):
        self.media = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.media, ignore_errors=True)
        override = override_settings(MEDIA_ROOT=self.media)
        override.enable()
        self.addCleanup(override.disable)
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("runner", password="x")

    def create(self, **extra):
        body = json.dumps({"params": PARAMS, **extra})
        with patch("npc_creator.views.floorplan.floorplan_job_async") as job:
            response = self.client.post(
                "/api/npc_creator/floorplans/", body, content_type="application/json"
            )
        return response, job

    def listed(self):
        response = self.client.get("/api/npc_creator/entities/", {"kind[]": "Floorplan"})
        return [entity["id"] for entity in response.json()["results"]]

    def create_and_render(self):
        response, job = self.create()
        generation = FloorplanGeneration.objects.get(
            entity__uuid=response.json()["id"]
        )
        floorplan_job(generation.id)
        return response.json()["id"]

    def test_create_queues_a_job(self):
        response, job = self.create()

        self.assertEqual(201, response.status_code)
        self.assertEqual("queued", response.json()["status"]["state"])
        job.assert_called_once()
        floorplan = Floorplan.objects.get(uuid=response.json()["id"])
        self.assertEqual(Entity.Kinds.FLOORPLAN, floorplan.kind)
        self.assertEqual("office 30x20", floorplan.attributes["name"])

    def test_same_parameters_reuse_the_existing_floorplan(self):
        first, _ = self.create()
        second, job = self.create()

        self.assertEqual(200, second.status_code)
        self.assertEqual(first.json()["id"], second.json()["id"])
        self.assertTrue(second.json()["existing"])
        job.assert_not_called()
        self.assertEqual(1, Floorplan.objects.count())

    def test_other_parameters_or_a_failed_render_make_a_new_floorplan(self):
        first, _ = self.create()
        other, _ = self.create(language="en")
        self.assertNotEqual(first.json()["id"], other.json()["id"])

        FloorplanGeneration.objects.update(state=FloorplanGeneration.State.FAILED)
        retry, job = self.create()
        self.assertEqual(201, retry.status_code)
        job.assert_called_once()

    def test_create_records_the_creator(self):
        self.client.force_authenticate(self.user)

        response, _ = self.create()

        self.assertEqual(
            self.user, Floorplan.objects.get(uuid=response.json()["id"]).creator
        )

    def test_create_rejects_invalid_requests(self):
        for body in ("nope", json.dumps({"params": {**PARAMS, "width": 999}})):
            with self.subTest(body):
                response = self.client.post(
                    "/api/npc_creator/floorplans/", body, content_type="application/json"
                )

                self.assertEqual(400, response.status_code)
        self.assertEqual(0, Floorplan.objects.count())

    def test_job_renders_files(self):
        uuid = self.create_and_render()

        status = self.client.get(f"/api/npc_creator/floorplans/{uuid}/status/").json()
        self.assertEqual("done", status["state"])
        self.assertEqual(3, status["steps_total"])
        self.assertEqual(3, status["steps_done"])

        detail = self.client.get(f"/api/npc_creator/floorplans/{uuid}/").json()
        self.assertEqual([0, 1], [floor["level"] for floor in detail["floors"]])
        for floor in detail["floors"]:
            self.assertTrue(floor["image_url"].endswith(".webp"))
            self.assertTrue(floor["dd2vtt_url"].endswith(".dd2vtt"))
        self.assertTrue(detail["building_url"].endswith(".json"))
        floorplan = Floorplan.objects.get(uuid=uuid)
        self.assertEqual(2, floorplan.image_set.count())
        self.assertEqual(
            2, floorplan.floorplan_files.filter(kind=FloorplanFile.Kind.DD2VTT).count()
        )

    def test_impossible_building_fails_with_roomplanners_message(self):
        response, _ = self.create()
        floorplan = Floorplan.objects.get(uuid=response.json()["id"])
        floorplan.attributes = {
            **floorplan.attributes,
            "params": {**floorplan.attributes["params"], "shape": "l", "width": 8, "depth": 8},
        }
        floorplan.save()
        generation = FloorplanGeneration.objects.get(entity=floorplan)

        floorplan_job(generation.id)

        generation.refresh_from_db()
        self.assertEqual("failed", generation.state)
        self.assertNotEqual("", generation.error)
        self.assertNotEqual("Floorplan generation failed.", generation.error)

    def test_publish_requires_a_finished_floorplan(self):
        response, _ = self.create()

        published = self.client.post(f"/api/npc_creator/floorplans/{response.json()['id']}/publish/")

        self.assertEqual(409, published.status_code)

    def test_publish_makes_it_listed_and_locks_it(self):
        uuid = self.create_and_render()
        self.assertEqual([], self.listed())

        self.assertEqual(200, self.client.post(f"/api/npc_creator/floorplans/{uuid}/publish/").status_code)

        self.assertEqual([uuid], self.listed())
        self.assertEqual(
            403, self.client.post(f"/api/npc_creator/floorplans/{uuid}/publish/").status_code
        )

    def test_only_the_creator_publishes(self):
        self.client.force_authenticate(self.user)
        uuid = self.create_and_render()
        other = get_user_model().objects.create_user("other", password="x")
        self.client.force_authenticate(other)

        response = self.client.post(f"/api/npc_creator/floorplans/{uuid}/publish/")

        self.assertEqual(403, response.status_code)

    def test_options_lists_caps_and_themes(self):
        options = self.client.get("/api/npc_creator/floorplans/options/").json()

        self.assertEqual(["neon2", "modern2"], options["themes"])
        self.assertIn("office", options["building_types"])
        self.assertEqual([1, 6], options["limits"]["floors_above"])

    def test_options_name_rooms_in_the_requested_language(self):
        german = self.client.get("/api/npc_creator/floorplans/options/?lang=de").json()
        english = self.client.get("/api/npc_creator/floorplans/options/?lang=en").json()
        unknown = self.client.get("/api/npc_creator/floorplans/options/?lang=fr").json()

        self.assertEqual("Schlafzimmer", german["names"]["rooms"]["bedroom"])
        self.assertNotEqual(
            german["names"]["rooms"]["bedroom"], english["names"]["rooms"].get("bedroom")
        )
        self.assertEqual(german["names"], unknown["names"])

    def test_unknown_floorplan_is_404(self):
        response = self.client.get("/api/npc_creator/floorplans/00000000-0000-0000-0000-000000000000/")

        self.assertEqual(404, response.status_code)
