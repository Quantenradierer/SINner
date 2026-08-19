import unittest

from npc_creator.game_mechanics.manager import ALL_RULES
from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.sr6.gear_collection import GearCollection
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.game_mechanics.sr6.rule import Rule
from npc_creator.game_mechanics.sr6.source import Source


def make_gear(**overrides) -> Gear:
    defaults = dict(
        type=ObjectType.Weapon,
        id="test/weapon",
        gear=GearCollection(),
        source=Source(page=1, book="SR6Core"),
        cost=0,
        avail="0",
    )
    defaults.update(overrides)
    return Gear(**defaults)


def make_rule(id: str, modifier_type: str, modification: str, modifies: str) -> Rule:
    return Rule(
        id=id,
        modifies=modifies,
        modifier_type=modifier_type,
        modification=modification,
        source=Source(page=1, book="SR6Core"),
    )


class TestApplyRuleOrdering(unittest.TestCase):
    """Regression test: apply_rule must sort each ModifiableValue's mods by
    modifier type (BASE, REPLACEMENT, ADD, LIMIT) regardless of the order in
    which the rules were applied - that ordering is what the whole rule
    engine relies on to compute the correct final value."""

    def test_mods_are_evaluated_base_add_limit_regardless_of_apply_order(self):
        weapon = make_gear()

        limit_rule = make_rule("limit", "LIMIT", "min(value, 5)", "weapon.damage")
        add_rule = make_rule("add", "ADD", "4", "weapon.damage")
        base_rule = make_rule("base", "BASE", "2", "weapon.damage")

        # Apply deliberately out of BASE/REPLACEMENT/ADD/LIMIT order.
        weapon.apply_rule(limit_rule)
        weapon.apply_rule(add_rule)
        weapon.apply_rule(base_rule)

        self.assertEqual(
            [mod.modifier_type for mod in weapon.damage.mods],
            ["BASE", "ADD", "LIMIT"],
        )
        self.assertEqual(weapon.damage.mod, 5)

    def test_replacement_is_applied_before_add_and_limit(self):
        weapon = make_gear()

        weapon.apply_rule(make_rule("add", "ADD", "4", "weapon.damage"))
        weapon.apply_rule(make_rule("repl", "REPLACEMENT", "10", "weapon.damage"))
        weapon.apply_rule(make_rule("base", "BASE", "2", "weapon.damage"))

        # REPLACEMENT (10) overrides BASE (2), then ADD stacks on top of it.
        self.assertEqual(weapon.damage.mod, 14)


class TestApplyRuleEvalModifiesList(unittest.TestCase):
    def test_a_rule_can_target_multiple_values_at_once(self):
        weapon = make_gear()
        rule = make_rule(
            "both",
            "ADD",
            "1",
            "[weapon.damage, weapon.attack_dices]",
        )
        weapon.apply_rule(rule)
        self.assertEqual(weapon.damage.mod, 1)
        self.assertEqual(weapon.attack_dices.mod, 1)


class TestAddGear(unittest.TestCase):
    RULE_ID = "test/add-gear-context-rule"

    def setUp(self):
        self.rule = make_rule(
            self.RULE_ID, "ADD", "character.attributes.body.mod", "weapon.damage"
        )
        ALL_RULES.add(self.rule)

    def tearDown(self):
        del ALL_RULES.data[self.RULE_ID]

    def test_wear_rules_can_reach_into_the_wearers_context(self):
        from npc_creator.game_mechanics.sr6.character import SR6Character

        character = SR6Character(
            uuid="test-uuid",
            name="Test",
            street_name="Testy",
            size="medium",
            weight="70kg",
            age="30",
            gender="other",
            metatype="human",
            unarmed=make_gear(id="test/unarmed"),
        )
        character.attributes.body.points = 3

        weapon = make_gear(wear_rules=[self.RULE_ID])
        character.add_gear(weapon)

        self.assertIn(weapon, character.gear)
        self.assertEqual(weapon.damage.mod, 3)
