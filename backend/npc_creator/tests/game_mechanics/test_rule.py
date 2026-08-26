import unittest

from npc_creator.game_mechanics.sr6.eval_errors import NotExistingAttributeError
from npc_creator.game_mechanics.sr6.rule import Rule
from npc_creator.game_mechanics.sr6.source import Source


def make_rule(
    modifier_type: str,
    modification: str,
    context: dict | None = None,
    enable: str | None = None,
) -> Rule:
    return Rule(
        id=f"test/{modifier_type.lower()}",
        modifies="character.foo",
        modifier_type=modifier_type,
        modification=modification,
        enable=enable,
        source=Source(page=1, book="SR6Core"),
        context=context or {},
    )


class TestRuleCalcBase(unittest.TestCase):
    def test_base_ignores_current_value(self):
        rule = make_rule("BASE", "2")
        self.assertEqual(rule.calc(999), 2)

    def test_base_can_use_expression(self):
        rule = make_rule("BASE", "1 + 1")
        self.assertEqual(rule.calc(0), 2)


class TestRuleCalcReplacement(unittest.TestCase):
    def test_replacement_ignores_current_value(self):
        rule = make_rule("REPLACEMENT", "4")
        self.assertEqual(rule.calc(2), 4)


class TestRuleCalcAdd(unittest.TestCase):
    def test_add_adds_to_current_value(self):
        rule = make_rule("ADD", "4")
        self.assertEqual(rule.calc(2), 6)

    def test_add_can_be_negative(self):
        rule = make_rule("ADD", "-3")
        self.assertEqual(rule.calc(5), 2)


class TestRuleCalcLimit(unittest.TestCase):
    def test_limit_clamps_value_downward(self):
        rule = make_rule("LIMIT", "min(value, 5)")
        self.assertEqual(rule.calc(9), 5)

    def test_limit_leaves_value_untouched_when_within_range(self):
        rule = make_rule("LIMIT", "min(value, 5)")
        self.assertEqual(rule.calc(3), 3)

    def test_limit_can_reference_value_in_a_compound_expression(self):
        # regression: the modification's `value` must be the value flowing
        # through the pipeline, and the clamped result must actually be used.
        rule = make_rule("LIMIT", "max(0, min(value, 6))")
        self.assertEqual(rule.calc(-2), 0)
        self.assertEqual(rule.calc(10), 6)


class TestRuleCalcMissingAttribute(unittest.TestCase):
    class _RaisesOnAccess:
        @property
        def missing(self):
            raise NotExistingAttributeError()

    def test_missing_attribute_leaves_value_unchanged(self):
        rule = make_rule(
            "ADD", "dummy.missing", context={"dummy": self._RaisesOnAccess()}
        )
        self.assertEqual(rule.calc(7), 7)


class TestRuleCalcEnable(unittest.TestCase):
    def test_no_enable_condition_always_applies(self):
        rule = make_rule("ADD", "4")
        self.assertEqual(rule.calc(2), 6)

    def test_true_condition_applies_the_rule(self):
        rule = make_rule("ADD", "4", context={"flag": True}, enable="flag")
        self.assertEqual(rule.calc(2), 6)

    def test_false_condition_leaves_value_unchanged(self):
        rule = make_rule("ADD", "4", context={"flag": False}, enable="flag")
        self.assertEqual(rule.calc(2), 2)

    def test_unevaluable_condition_is_treated_as_disabled(self):
        # regression: enable referencing gear/state not wired into this
        # object's context must not crash rule application - it should
        # just behave as if the condition wasn't met.
        rule = make_rule("ADD", "4", context={}, enable="weapon.smartlink_active")
        self.assertEqual(rule.calc(2), 2)


class TestRuleEvalModifies(unittest.TestCase):
    def test_wraps_single_result_in_a_list(self):
        rule = make_rule("BASE", "1")
        rule = rule.model_copy(update={"modifies": "'a'"})
        self.assertEqual(rule.eval_modifies({}), ["a"])

    def test_passes_through_list_results(self):
        rule = make_rule("BASE", "1")
        rule = rule.model_copy(update={"modifies": "['a', 'b']"})
        self.assertEqual(rule.eval_modifies({}), ["a", "b"])

    def test_modifies_types_reads_the_object_type_prefix(self):
        from npc_creator.game_mechanics.sr6.object_type import ObjectType

        rule = make_rule("BASE", "1").model_copy(
            update={"modifies": "character.attributes.body"}
        )
        self.assertEqual(rule.modifies_types, ObjectType.Character)
