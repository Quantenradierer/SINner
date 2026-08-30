from npc_creator.game_mechanics.manager import ALL_GEAR, GearManager
from npc_creator.game_mechanics.named_list_with_mods import (
    as_jsonable,
    get_minimal_gear_list,
)
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.operations.gpt import entity
import json


class GenericFill(entity.Fill):
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
- Felder wie 'metatype' und 'gender' enthalten den deutschen, lesbaren Begriff (z.B. "Mensch", "Männlich"). Die zugehörigen '*_enum'-Felder enthalten den englischen Wert aus der Auswahlliste im Kommentar (z.B. "human", "male"). Übernimm nicht den englischen enum-Wert in das lesbare Feld.
- Antworte im JSON-Format, und achte auf die Datentypen
- Antworte im selben Format, was dir gegeben wird. Füge keine verschalteten Datenstukturen hinzu, außer es wird explizit beschrieben
"""
