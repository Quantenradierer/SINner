from npc_creator.game_mechanics.armor import armor_loader
from npc_creator.game_mechanics.weapons import weapon_loader
from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.services.interpret_gpt import dict_from_text
from npc_creator.operations.gpt import entity
import json


class Fill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = f"""- Vervollständige einen NPC für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Erstelle unangemessene, extreme, rassistische oder homophobe NPC so, das du zeigst wie falsch ihre Werte sind 
- Erstelle keine Urheberrechtlich geschützten Figuren oder Personen
- Erstelle keine Runner oder Söldner, sofern nicht anders gewünscht
- Das Geheimnis muss detailliert beschrieben sein
- Der Name ist in der Form 'Vorname "Rufname" Nachname' 
- Sei beim Namen kreativ
- Weniger Namen mit "Schatten", mehr Codenames und Spitznamen.
- Nutze seltene und unübliche Namen 
- Achte darauf, den NPC in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
- Zwerge sind keine Schmiede oder Braumeister, sondern gehen reguläre Berufe der Modernen Zeit nach
- Elfen sind maximal 70 Jahre alt
- Erstelle standardmäßig weniger Personen mit afro-Ethnizität
- Beachte die geänderte Weltordnung, Länder und Regionen der Sechsten Welt von Shadowrun, wie: ADL, CAS, CFS, Japanisches Kaiserreich, Tír na nÓg, Tír Tairngire oder UCAS
- Die Werte (Attribute und Skills) dürfen höher ausfallen wenn es für die Person Sinn ergibt 
- Antworte in Deutsch
- Antworte im JSON-Format, und achte auf die Datentypen
- Fast jeder trägt eine Waffe

Folgendes ist eine Liste der Waffen, gib in der Antwort nur die ID an:
    {json.dumps(list(self._weapons()))}
    
    
Folgendes ist eine Liste der Rüstzeug, gib in der Antwort nur die ID an:
    {json.dumps(list(self._armors()))}
"""
        print({json.dumps(list(self._weapons()))})

    def _weapons(self):
        for weapon in weapon_loader.weapons.values():
            yield {
                "id": weapon.id,
                "name": weapon.name,
                "subtype": weapon.subtype,
            }

    def _armors(self):
        for armor in armor_loader.armors.values():
            yield {
                "id": armor.id,
                "name": armor.name,
                "subtype": armor.subtype,
            }
