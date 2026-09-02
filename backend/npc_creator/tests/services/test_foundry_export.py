import json

from django.test import TestCase

from npc_creator.models.entities.npc import Npc
from npc_creator.services.exporter.foundry import ExportError, foundry_json
from npc_creator.services.exporter.foundry_template import RootNPC

WEAPON_ID = "sr6core/weapon/streetline special"
ARMOR_ID = "sr6core/armor/helmet"
CYBERWARE_ID = "sr6core/cyberware/bone_lacing_aluminum"  # 1.0 essence
COMMLINK_ID = "sr6core/commlink/2"


def clean_values(**overrides):
    values = {
        "name": "Testrunner",
        "profession": "Söldner",
        "metatype_enum": "ork",
        "gender_enum": "male",
        "constitution": 3,
        "agility": 4,
        "reaction": 5,
        "strength": 6,
        "willpower": 2,
        "logic": 3,
        "intuition": 3,
        "charisma": 2,
        "edge": 4,
        "magic": 0,
        "resonance": 0,
        "equipment": [WEAPON_ID, ARMOR_ID, CYBERWARE_ID, COMMLINK_ID],
    }
    for name in (
        "astral athletics biotech close_combat con conjuring cracking electronics "
        "enchanting engineering exotic_weapons firearms influence outdoors perception "
        "piloting sorcery stealth tasking"
    ).split():
        values[f"skill_{name}"] = 1
    values["skill_firearms"] = 4
    values.update(overrides)
    return values


class FoundryExportTest(TestCase):
    def make_npc(self, **overrides):
        npc = Npc(attributes=clean_values(**overrides))
        npc.save()
        return npc

    def export(self, **overrides):
        return json.loads(foundry_json(self.make_npc(**overrides)))

    def test_output_validates_against_eden_template(self):
        RootNPC.model_validate_json(foundry_json(self.make_npc()))

    def test_v10_data_model_root_key(self):
        data = self.export()
        # Foundry actor type must match eden's Actor.types entry exactly ("NPC").
        self.assertEqual("NPC", data["type"])
        self.assertEqual("npc", data["system"]["type"])
        self.assertIn("system", data)
        self.assertNotIn("data", data)

    def test_attributes_and_skills_land(self):
        system = self.export()["system"]
        self.assertEqual(3, system["attributes"]["bod"]["base"])
        self.assertEqual(6, system["attributes"]["str"]["pool"])
        self.assertEqual(4, system["skills"]["firearms"]["points"])
        self.assertEqual(1, system["skills"]["stealth"]["points"])

    def test_metatype_passed_through(self):
        self.assertEqual("ork", self.export()["system"]["metatype"])

    def test_mortype_derived(self):
        self.assertEqual("mundane", self.export()["system"]["mortype"])
        self.assertEqual("magician", self.export(magic=5)["system"]["mortype"])
        self.assertEqual(
            "technomancer", self.export(resonance=4)["system"]["mortype"]
        )

    def test_essence_reflects_cyberware(self):
        # 6.0 base - 1.0 for aluminium bone lacing
        self.assertEqual(5.0, self.export()["system"]["attributes"]["essence"]["base"])

    def test_gear_becomes_typed_items(self):
        items = self.export()["items"]
        by_type = {}
        for item in items:
            by_type.setdefault(item["system"]["type"], []).append(item)

        self.assertIn("WEAPON_FIREARMS", by_type)
        self.assertIn("ARMOR", by_type)
        self.assertIn("CYBERWARE", by_type)
        self.assertIn("ELECTRONICS", by_type)
        self.assertIn("WEAPON_CLOSE_COMBAT", by_type)  # auto-added unarmed

        weapon = by_type["WEAPON_FIREARMS"][0]
        self.assertEqual(2, weapon["system"]["dmg"])
        self.assertTrue(weapon["system"]["modes"]["SS"])
        self.assertEqual(WEAPON_ID, weapon["system"]["genesisID"])

        armor = by_type["ARMOR"][0]
        self.assertEqual(2, armor["system"]["defense"])

        unarmed = by_type["WEAPON_CLOSE_COMBAT"][0]
        self.assertEqual("UNARMED", unarmed["system"]["subtype"])
        self.assertEqual(11, unarmed["system"]["attackRating"][0])  # str 6 + rea 5

    def test_export_source_flag(self):
        npc = self.make_npc()
        data = json.loads(foundry_json(npc))
        self.assertEqual(
            str(npc.uuid), data["flags"]["exportSource"]["npc_uuid"]
        )

    # --- strict precondition -------------------------------------------------
    def test_missing_skill_is_rejected(self):
        values = clean_values()
        del values["skill_firearms"]
        with self.assertRaises(ExportError):
            foundry_json(Npc(attributes=values))

    def test_missing_attribute_is_rejected(self):
        values = clean_values()
        del values["strength"]
        with self.assertRaises(ExportError):
            foundry_json(Npc(attributes=values))

    def test_invalid_metatype_is_rejected(self):
        with self.assertRaises(ExportError):
            foundry_json(Npc(attributes=clean_values(metatype_enum="orc")))

    def test_prose_equipment_is_rejected(self):
        with self.assertRaises(ExportError):
            foundry_json(
                Npc(attributes=clean_values(equipment="Cyberdeck, Tablet, Pistole"))
            )

    def test_unresolvable_equipment_id_is_rejected(self):
        with self.assertRaises(ExportError):
            foundry_json(
                Npc(attributes=clean_values(equipment=[WEAPON_ID, "tool_001"]))
            )

    def test_non_numeric_skill_is_rejected(self):
        with self.assertRaises(ExportError):
            foundry_json(
                Npc(attributes=clean_values(skill_firearms="ziemlich gut"))
            )
