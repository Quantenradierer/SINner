import unittest

from npc_creator.game_mechanics.manager import ALL_GEAR


class TestAttackRatingLoadsFromData(unittest.TestCase):
    """Regression test for the attack_rating -> attack_rating_0..4 migration."""

    def test_weapon_attack_rating_brackets_load_correctly(self):
        weapon = ALL_GEAR["sr6core/weapon/fichetti tiffani needler"]

        self.assertEqual(weapon.attack_rating_0.mod, 10)
        self.assertEqual(weapon.attack_rating_1.mod, 6)
        self.assertEqual(weapon.attack_rating_2.mod, 2)
        self.assertEqual(weapon.attack_rating_3.mod, 0)
        self.assertEqual(weapon.attack_rating_4.mod, 0)
