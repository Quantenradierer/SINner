import json

from django.test import TestCase

from npc_creator.models.entities.npc import Npc
from npc_creator.services.exporter.foundry import ExportError
from npc_creator.services.exporter.roll20 import roll20_json
from npc_creator.services.exporter.roll20_templates import R20Character
from npc_creator.tests.services.test_foundry_export import (
    ARMOR_ID,
    COMMLINK_ID,
    CYBERWARE_ID,
    WEAPON_ID,
    clean_values,
)


class Roll20ExportTest(TestCase):
    def make_npc(self, **overrides):
        npc = Npc(attributes=clean_values(**overrides))
        npc.save()
        return npc

    def export(self, **overrides):
        return json.loads(roll20_json(self.make_npc(**overrides)))

    def test_output_validates_against_template(self):
        R20Character.model_validate_json(roll20_json(self.make_npc()))

    def test_envelope(self):
        data = self.export()
        self.assertEqual("SHADOWRUN6", data["system"])
        self.assertEqual("3.2.0", data["version"])
        # the Roll20 importer expects every section key, even when empty
        for key in ("spells", "vehicles", "contacts", "lifestyles", "qualities"):
            self.assertEqual([], data[key])

    def test_attributes_pass_through(self):
        rows = {a["id"]: a for a in self.export()["attributes"]}
        self.assertEqual(17, len(rows))
        # no attribute-boosting gear -> modifiedValue == points. The fixture
        # carries bone lacing, which raises damage resistance, NOT the Body
        # attribute (SR6 GRW p. 288 "Kompositknochen").
        self.assertEqual(3, rows["BODY"]["points"])
        self.assertEqual(3, rows["BODY"]["modifiedValue"])
        self.assertEqual(6, rows["STRENGTH"]["modifiedValue"])

    def test_derived_pools_are_computed(self):
        rows = {a["id"]: a for a in self.export()["attributes"]}
        for key in (
            "DEFENSE_POOL_PHYSICAL",
            "COMPOSURE",
            "JUDGE_INTENTIONS",
            "MEMORY",
            "LIFT_CARRY",
        ):
            self.assertEqual(0, rows[key]["points"])
            self.assertGreater(rows[key]["modifiedValue"], 0)

    def test_initiatives(self):
        rows = {i["id"]: i for i in self.export()["initiatives"]}
        self.assertEqual(5, len(rows))
        self.assertRegex(rows["INITIATIVE_PHYSICAL"]["dice"], r"^\+\d+D6$")
        self.assertGreater(rows["INITIATIVE_PHYSICAL"]["value"], 0)

    def test_all_skills_present_with_rating(self):
        rows = {s["id"]: s for s in self.export()["skills"]}
        self.assertEqual(19, len(rows))
        self.assertEqual(4, rows["firearms"]["rating"])
        self.assertEqual("Geschicklichkeit", rows["firearms"]["attribute"])
        self.assertEqual(1, rows["stealth"]["rating"])

    def test_metatype_prefers_german_free_text(self):
        self.assertEqual("Ork", self.export(metatype="Ork")["metaType"])
        # falls back to the enum when the readable field is absent
        self.assertEqual("ork", self.export()["metaType"])

    def test_gender_mapping(self):
        self.assertEqual("MALE", self.export()["gender"])
        self.assertEqual("DIVERSE", self.export(gender_enum="divers")["gender"])

    def test_street_name_from_quoted_handle(self):
        data = self.export(name='Jane "Spark" Doe')
        self.assertEqual("Spark", data["streetName"])
        # Genesis keeps the legal name and the handle apart
        self.assertEqual("Jane Doe", data["name"])
        self.assertEqual("", self.export(name="Jane Doe")["streetName"])

    def test_fire_mode_codes(self):
        # semi-auto pistol -> single Genesis code, comma-joined when multiple
        weapon = self.export()["longRangeWeapons"][0]
        self.assertRegex(weapon["mode"], r"^[A-Z]{2}(,[A-Z]{2})*$")

    def test_gear_lands_in_the_right_sections(self):
        data = self.export()

        weapon = data["longRangeWeapons"][0]
        self.assertEqual("Feuerwaffen", weapon["type"])
        self.assertEqual("2K", weapon["damage"])
        self.assertRegex(weapon["attackRating"], r"^[\d-]+(/[\d-]+){4}$")
        self.assertEqual("EM", weapon["mode"])
        self.assertGreater(weapon["pool"], 0)

        unarmed = data["closeCombatWeapons"][0]
        self.assertEqual("Unbewaffnet", unarmed["name"])
        self.assertNotIn("mode", unarmed)

        self.assertEqual(2, data["armors"][0]["rating"])
        self.assertTrue(data["armors"][0]["primary"])
        self.assertEqual(-4, data["armors"][0]["socialrating"])  # helmet

        self.assertEqual(1.0, data["augmentations"][0]["essence"])

        matrix = data["matrixItems"][0]
        self.assertEqual("COMMLINK", matrix["subType"])
        self.assertEqual(2, matrix["deviceRating"])

    def test_armor_social_rating(self):
        # values from Feuer frei! p. 177 (social table for the core armor)
        data = self.export(
            equipment=[
                "sr6core/armor/armor vest",
                "sr6core/armor/armor clothing",
            ]
        )
        armors = {a["name"]: a for a in data["armors"]}
        self.assertEqual(-1, armors["Panzerweste"]["socialrating"])
        self.assertEqual(3, armors["Panzerweste"]["rating"])
        # Panzerkleidung has no social modifier ("-" in the table)
        self.assertEqual(0, armors["Panzerkleidung"]["socialrating"])

    # --- strict precondition (shared with the Foundry exporter) -------------
    def test_missing_skill_is_rejected(self):
        values = clean_values()
        del values["skill_firearms"]
        with self.assertRaises(ExportError):
            roll20_json(Npc(attributes=values))

    def test_invalid_metatype_is_rejected(self):
        with self.assertRaises(ExportError):
            roll20_json(Npc(attributes=clean_values(metatype_enum="orc")))

    def test_prose_equipment_is_rejected(self):
        with self.assertRaises(ExportError):
            roll20_json(
                Npc(attributes=clean_values(equipment="Cyberdeck, Tablet, Pistole"))
            )
