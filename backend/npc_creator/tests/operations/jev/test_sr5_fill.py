import json
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import patch

from npc_creator.game_mechanics.sr5.skills import MAGICAL_KEYS, SKILL_NAMES, skill_key
from npc_creator.models.entities.npc import Npc, SR5Attributes, SR6Attributes
from npc_creator.operations.jev.sr5_fill import JevSr5Fill, build_questions
from npc_creator.operations.jev.sr6_fill import LEVELS

CORE = [name for name in SR5Attributes.model_fields if name not in SKILL_NAMES]


def fake_client(scores, calls):
    class Client:
        def __init__(self, **kwargs):
            pass

        def system_one(self, state, questions):
            calls.append((state, list(questions)))
            return SimpleNamespace(
                request_id="r",
                usage=None,
                scores={name: SimpleNamespace(score=scores.get(name, 0.2)) for name in questions},
            )

    return Client


class TestSr5Schema(TestCase):
    def test_75_skills_with_unique_prefixed_keys(self):
        self.assertEqual(75, len(SKILL_NAMES))
        self.assertTrue(all(key.startswith("sr5_skill_") for key in SKILL_NAMES))
        self.assertEqual("sr5_skill_free_fall", skill_key("Free-Fall"))

    def test_shares_the_core_attributes_with_sr6(self):
        sr6_core = [name for name in SR6Attributes.model_fields if not name.startswith("skill_")]
        self.assertEqual(sr6_core, CORE)
        self.assertEqual(11, len(CORE))

    def test_skill_keys_do_not_collide_with_sr6(self):
        self.assertFalse(set(SKILL_NAMES) & set(SR6Attributes.model_fields))


class TestSr5Questions(TestCase):
    def test_one_score_per_skill_on_the_shared_rubric(self):
        questions = build_questions(list(SKILL_NAMES))
        self.assertEqual(list(SKILL_NAMES), list(questions))
        for question in questions.values():
            self.assertEqual("score", question.type)
            self.assertEqual(LEVELS, list(question.criteria))

    def test_magical_skills_are_hinted_to_stay_zero(self):
        question = build_questions(MAGICAL_KEYS)[MAGICAL_KEYS[0]]
        self.assertIn("magic", question.instructions)


class TestSr5Fill(TestCase):
    def entity(self, attributes):
        entity = Npc(prompt="a street samurai")
        entity.attributes = dict(attributes)
        return entity

    def run_fill(self, entity, scores=None):
        calls = []
        with patch("npc_creator.operations.jev.sr6_fill.TypeSafeClient", fake_client(scores or {}, calls)), \
             patch.object(Npc, "save"), patch.object(Npc, "refresh_from_db"), \
             patch("npc_creator.operations.jev.sr6_fill.GptRequest"):
            result = JevSr5Fill(entity=entity).call()
        return result, calls

    def test_rates_skills_and_rounds_them(self):
        core = {name: 3 for name in CORE}
        entity = self.entity(core)
        result, calls = self.run_fill(entity, {skill_key("Pistols"): 5.6})
        self.assertTrue(result)
        self.assertEqual(1, len(calls))
        self.assertEqual(list(SKILL_NAMES), calls[0][1])
        self.assertEqual(6, entity.attributes[skill_key("Pistols")])
        self.assertEqual(0, entity.attributes[skill_key("Archery")])
        self.assertEqual(3, entity.attributes["agility"])
        self.assertEqual(3, calls[0][0]["npc"]["agility"])

    def test_missing_attributes_are_rated_first_and_seen_by_the_skills(self):
        entity = self.entity({})
        result, calls = self.run_fill(entity, {"agility": 4.2})
        self.assertTrue(result)
        self.assertEqual(2, len(calls))
        self.assertEqual(CORE, calls[0][1])
        self.assertEqual(4, calls[1][0]["npc"]["agility"])
        self.assertTrue(entity.schema_complete("sr5"))

    def test_complete_entity_is_left_alone(self):
        entity = self.entity({name: 1 for name in SR5Attributes.model_fields})
        result, calls = self.run_fill(entity)
        self.assertTrue(result)
        self.assertEqual([], calls)
