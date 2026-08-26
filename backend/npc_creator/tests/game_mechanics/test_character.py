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

    def test_astral_initiative_dices_matches_the_book_errata(self):
        # SR6 core errata (2nd->3rd printing): astral initiative is
        # Logic + Intuition + 3W6, not the pre-errata 2W6.
        self.assertEqual(self.character.astral_initiative_dices.mod, 3)

    def test_matrix_vr_cold_sim_initiative_dices(self):
        self.assertEqual(self.character.initiative_matrix_vr_cold_dices.mod, 2)

    def test_matrix_vr_hot_sim_initiative_dices(self):
        self.assertEqual(self.character.initiative_matrix_vr_hot_dices.mod, 3)


class TestCyberjackMatrixInitiativeBonus(unittest.TestCase):
    """Regression test for the errata-driven cyberjack rewrite: the bonus
    is dice added to both VR modes, not a flat bonus to the AR/VR base
    values, and only ratings 1-3 give +1 / 4-6 give +2 (not +1/+2/+3)."""

    def setUp(self):
        self.character = make_character()
        self.character.enable_base_rules()

    def test_low_rating_cyberjack_adds_one_die_to_both_vr_modes(self):
        from npc_creator.game_mechanics.manager import ALL_GEAR

        cold_before = self.character.initiative_matrix_vr_cold_dices.mod
        hot_before = self.character.initiative_matrix_vr_hot_dices.mod

        cyberjack = ALL_GEAR["sr6core/cyberware/cyberjack/1"].model_copy(deep=True)
        self.character.add_gear(cyberjack)

        self.assertEqual(
            self.character.initiative_matrix_vr_cold_dices.mod, cold_before + 1
        )
        self.assertEqual(
            self.character.initiative_matrix_vr_hot_dices.mod, hot_before + 1
        )

    def test_high_rating_cyberjack_adds_two_dice_to_both_vr_modes(self):
        from npc_creator.game_mechanics.manager import ALL_GEAR

        cold_before = self.character.initiative_matrix_vr_cold_dices.mod
        hot_before = self.character.initiative_matrix_vr_hot_dices.mod

        cyberjack = ALL_GEAR["sr6core/cyberware/cyberjack/4"].model_copy(deep=True)
        self.character.add_gear(cyberjack)

        self.assertEqual(
            self.character.initiative_matrix_vr_cold_dices.mod, cold_before + 2
        )
        self.assertEqual(
            self.character.initiative_matrix_vr_hot_dices.mod, hot_before + 2
        )
