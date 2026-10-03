import unittest
from types import SimpleNamespace

from npc_creator.models.entities.npc import SR6Attributes
from npc_creator.operations.jev.sr6_fill import LEVELS, build_questions


class TestSr6Questions(unittest.TestCase):
    def test_one_score_per_field_on_the_shared_rubric(self):
        fields = list(SR6Attributes.model_fields)
        questions = build_questions(fields)
        self.assertEqual(fields, list(questions))
        for question in questions.values():
            self.assertEqual("score", question.type)
            self.assertEqual(LEVELS, list(question.criteria))

    def test_rubric_runs_zero_to_nine(self):
        self.assertEqual(10, len(LEVELS))


class TestRounding(unittest.TestCase):
    def test_scores_are_rounded_to_int(self):
        answers = SimpleNamespace(scores={"agility": SimpleNamespace(score=3.6)})
        self.assertEqual(4, round(answers.scores["agility"].score))
