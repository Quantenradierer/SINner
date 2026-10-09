from npc_creator.game_mechanics.manager import ALL_GEAR, GearManager
from npc_creator.game_mechanics.named_list_with_mods import (
    as_jsonable,
    get_minimal_gear_list,
)
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.operations.gpt import entity
import json


ENGLISH_PROMPT = """- Complete an NPC for a Shadowrun pen & paper roleplaying game
- If no information is given, make some up
- Create inappropriate, extreme, racist or homophobic NPCs in a way that shows how wrong their values are
- Do not create copyrighted characters or real persons
- Do not create runners or mercenaries unless requested otherwise
- The secret must be described in detail
- The name has the form 'First name "Nickname" Last name'
- Be creative with names
- Fewer names with "Shadow", more codenames and nicknames
- Use rare and unusual names
- Integrate the NPC into the Shadowrun world and make them appealing for the players
- Dwarfs are not smiths or brewmasters, they have regular modern-day professions
- Elves are at most 70 years old
- By default, create fewer people of Afro ethnicity
- Respect the changed world order, countries and regions of the Sixth World of Shadowrun, such as: ADL, CAS, CFS, Japanese Imperial State, Tír na nÓg, Tír Tairngire or UCAS
- The values (attributes and skills) may be higher if it makes sense for the person
- Answer in English. Every text value must be English, whatever language the input is in
- Fields like 'metatype' and 'gender' contain the readable English term (e.g. "Human", "Male"). The matching '*_enum' fields contain the value from the list in the comment (e.g. "human", "male"). Do not copy the enum value into the readable field.
- Answer in JSON format and mind the data types
- Answer in the same format you are given. Do not add nested data structures unless explicitly described
"""


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
        if self.entity.language == self.entity.Languages.ENGLISH:
            self.system_prompt = ENGLISH_PROMPT
