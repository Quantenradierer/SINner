import unittest

from npc_creator.game_mechanics.sr6.character import SR6Character
from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.sr6.gear_collection import GearCollection
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.game_mechanics.sr6.source import Source


def make_unarmed() -> Gear:
    return Gear(
        type=ObjectType.Weapon,
        id="test/unarmed",
        gear=GearCollection(),
        source=Source(page=1, book="SR6Core"),
        cost=0,
        avail="0",
    )


def make_character() -> SR6Character:
    return SR6Character(
        uuid="test-uuid",
        name="Test",
        street_name="Testy",
        size="medium",
        weight="70kg",
        age="30",
        gender="other",
        metatype="human",
        unarmed=make_unarmed(),
    )


class TestEnableBaseRules(unittest.TestCase):
    """End-to-end sanity check that the real sr6core rule data (loaded by
    the app's startup()) still produces the documented SR6 formulas once
    run through the rule engine."""

    def setUp(self):
        self.character = make_character()
        self.character.attributes.body.points = 4
        self.character.attributes.reaction.points = 3
        self.character.attributes.intuition.points = 2
        self.character.attributes.willpower.points = 5
        self.character.attributes.logic.points = 1
        self.character.skills.close_combat.points = 3
        self.character.enable_base_rules()

    def test_physical_initiative_dices_defaults_to_one(self):
        self.assertEqual(self.character.physical_initiative_dices.mod, 1)

    def test_physical_initiative_base_sums_dices_reaction_and_intuition(self):
        # dices(1) + reaction(3) + intuition(2)
        self.assertEqual(self.character.physical_initiative_base.mod, 6)

    def test_defense_rating_equals_body(self):
        self.assertEqual(self.character.defense_rating.mod, 4)

    def test_defense_pool_physical_sums_reaction_and_intuition(self):
        self.assertEqual(self.character.defense_pool_physical.mod, 5)

    def test_skill_specialisations_inherit_from_their_parent_skill(self):
        self.assertEqual(self.character.skills.close_combat.blades.mod, 3)
