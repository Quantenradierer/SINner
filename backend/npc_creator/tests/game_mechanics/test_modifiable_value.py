import unittest

from npc_creator.game_mechanics.sr6.modifiable_value import (
    ModifiableValue,
    ModifiableValueStr,
)
from npc_creator.game_mechanics.sr6.rule import Rule
from npc_creator.game_mechanics.sr6.source import Source


def make_rule(id: str, modifier_type: str, modification: str) -> Rule:
    return Rule(
        id=id,
        modifies="character.foo",
        modifier_type=modifier_type,
        modification=modification,
        source=Source(page=1, book="SR6Core"),
    )


class TestModifiableValueShorthand(unittest.TestCase):
    def test_bare_int_becomes_points(self):
        value = ModifiableValue.model_validate(5)
        self.assertEqual(value.points, 5)
        self.assertEqual(value.mods, [])

    def test_no_mods_returns_points(self):
        value = ModifiableValue(points=3)
        self.assertEqual(value.mod, 3)


class TestModifiableValuePipeline(unittest.TestCase):
    def test_applies_mods_in_list_order(self):
        # BASE -> ADD -> LIMIT, already in the correct stacking order.
        value = ModifiableValue(
            points=0,
            mods=[
                make_rule("base", "BASE", "2"),
                make_rule("add", "ADD", "4"),
                make_rule("limit", "LIMIT", "min(value, 5)"),
            ],
        )
        self.assertEqual(value.mod, 5)

    def test_mods_out_of_order_produce_a_different_result(self):
        # ModifiableValue.mod trusts the order of self.mods as given -
        # ordering by modifier type is the responsibility of whoever builds
        # the list (ModifiableObject.apply_rule). This documents that the
        # pipeline is order-sensitive, which is exactly why that ordering
        # matters.
        in_order = ModifiableValue(
            points=0,
            mods=[
                make_rule("base", "BASE", "2"),
                make_rule("add", "ADD", "4"),
                make_rule("limit", "LIMIT", "min(value, 5)"),
            ],
        )
        out_of_order = ModifiableValue(
            points=0,
            mods=[
                make_rule("limit", "LIMIT", "min(value, 5)"),
                make_rule("add", "ADD", "4"),
                make_rule("base", "BASE", "2"),
            ],
        )
        self.assertEqual(in_order.mod, 5)
        self.assertNotEqual(out_of_order.mod, in_order.mod)


class TestModifiableValueStr(unittest.TestCase):
    def test_bare_str_becomes_value(self):
        value = ModifiableValueStr.model_validate("P")
        self.assertEqual(value.value, "P")

    def test_none_stays_none(self):
        value = ModifiableValueStr.model_validate(None)
        self.assertIsNone(value.value)

    def test_replacement_overrides_base_value(self):
        value = ModifiableValueStr(
            value="P",
            mods=[make_rule("repl", "REPLACEMENT", "'S'")],
        )
        self.assertEqual(value.mod, "S")
