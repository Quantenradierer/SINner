import unittest
from types import SimpleNamespace

from npc_creator.game_mechanics.manager import ALL_GEAR
from npc_creator.operations.jev.equipment_catalog import EquipmentCatalog
from npc_creator.operations.jev.equipment_fill import (
    NpcProfile,
    Selection,
    build_questions,
)

STREET_SAMURAI = NpcProfile(is_decker=False, is_awakened=False)
DECKER = NpcProfile(is_decker=True, is_awakened=False)
MAGE = NpcProfile(is_decker=False, is_awakened=True)


def fake_answers(questions, resources=0.0, nouls=None, choices=None):
    """Every Noul answers 0 and every Choice its first option unless overridden."""
    nouls = nouls or {}
    choices = choices or {}
    noul_answers, choice_answers = {}, {}
    for name, question in questions.items():
        if question.type == "noul":
            noul_answers[name] = SimpleNamespace(noul=nouls.get(name, 0.0))
        elif question.type == "choice":
            first = next(iter(question.criteria))
            choice_answers[name] = SimpleNamespace(choice=choices.get(name, first))
    return SimpleNamespace(
        nouls=noul_answers,
        choices=choice_answers,
        scores={"resources": SimpleNamespace(score=resources)},
    )


class TestEquipmentCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = EquipmentCatalog.build()

    def test_every_option_is_known_gear(self):
        for field in self.catalog.__dataclass_fields__:
            for entry in getattr(self.catalog, field):
                for gear_id in getattr(entry, "variants", [entry]):
                    self.assertIn(gear_id, ALL_GEAR)

    def test_rating_variants_collapse_into_one_group(self):
        medkit = next(g for g in self.catalog.field_gear if g.key.endswith("/medkit"))
        self.assertEqual(6, len(medkit.variants))
        self.assertTrue(medkit.variants[-1].endswith("/6"))

    def test_choices_fit_the_255_option_limit(self):
        for field in ("armor", "ranged", "sidearms", "melee"):
            self.assertLessEqual(len(getattr(self.catalog, field)), 255)

    def test_excluded_categories(self):
        field_gear = [g.key for g in self.catalog.field_gear]
        self.assertFalse(any("docwagon" in key for key in field_gear))
        self.assertFalse(any("/security/lock" in key for key in field_gear))
        self.assertTrue(any("restraints" in key for key in field_gear))
        cyberware = [g.key for g in self.catalog.cyberware]
        self.assertNotIn("sr6core/cyberware/headware_commlink", cyberware)


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.catalog = EquipmentCatalog.build()

    def test_non_decker_gets_no_deck_questions(self):
        questions = build_questions(self.catalog, STREET_SAMURAI)
        self.assertNotIn("device", questions)
        self.assertFalse(any(q.startswith("software:") for q in questions))
        self.assertFalse(any("cyberjack" in q for q in questions))

    def test_decker_gets_device_and_software(self):
        questions = build_questions(self.catalog, DECKER)
        self.assertIn("device", questions)
        self.assertTrue(any(q.startswith("software:") for q in questions))

    def test_awakened_get_no_cyberware_questions(self):
        questions = build_questions(self.catalog, MAGE)
        self.assertFalse(any(q.startswith("cyberware:") for q in questions))


class TestSelection(unittest.TestCase):
    def setUp(self):
        self.catalog = EquipmentCatalog.build()

    def select(self, profile, **answers):
        questions = build_questions(self.catalog, profile)
        return Selection(
            self.catalog, profile, fake_answers(questions, **answers)
        ).gear_ids()

    def test_minimal_npc_gets_armor_and_commlink_only(self):
        result = self.select(STREET_SAMURAI)
        self.assertEqual([self.catalog.armor[0], "sr6core/commlink/1"], result)

    def test_resources_set_the_rating(self):
        result = self.select(STREET_SAMURAI, resources=3.0)
        self.assertIn("sr6core/commlink/6", result)

    def test_weapon_needs_presence_noul(self):
        result = self.select(
            STREET_SAMURAI,
            nouls={"armed:sidearm": 0.9},
            choices={"sidearm": "sr6core/weapon/ares predator vi", "ranged": "sr6core/weapon/ak-97"},
        )
        self.assertIn("sr6core/weapon/ares predator vi", result)
        self.assertNotIn("sr6core/weapon/ak-97", result)

    def test_only_deckers_get_decks(self):
        result = self.select(DECKER, choices={"device": "cyberdeck"})
        self.assertIn("sr6core/cyberdeck/1", result)

    def test_eye_mods_need_cybereyes(self):
        smartlink = {"cyberware:sr6core/cyberwaremod/smartlink": 0.9}
        self.assertNotIn("sr6core/cyberwaremod/smartlink", self.select(STREET_SAMURAI, nouls=smartlink))

        eyes = {**smartlink, "cyberware:sr6core/cyberware/cybereyes": 0.9}
        self.assertIn("sr6core/cyberwaremod/smartlink", self.select(STREET_SAMURAI, nouls=eyes))

    def test_cyberware_stays_within_essence_budget(self):
        nouls = {f"cyberware:{g.key}": 0.9 for g in self.catalog.cyberware}
        result = self.select(STREET_SAMURAI, resources=3.0, nouls=nouls)
        essence = sum(ALL_GEAR[i].essence or 0 for i in result if "/cyberware" in i)
        self.assertLessEqual(essence, 5.0)

    def test_field_gear_is_capped_and_ranked(self):
        nouls = {f"gear:{g.key}": 0.3 for g in self.catalog.field_gear}
        nouls["gear:sr6core/breakingandentering/lockpickset"] = 0.9
        result = self.select(STREET_SAMURAI, nouls=nouls)
        field_gear = result[2:]
        self.assertEqual(10, len(field_gear))
        self.assertEqual("sr6core/breakingandentering/lockpickset", field_gear[0])
