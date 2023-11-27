import json

from npc_creator.operations.gpt import entity


class Fill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_json = True
        self.system_prompt = """- Vervollständige eine Location für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Achte darauf, den NPC in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
- Sei beim Namen kreativ, nicht nur Neon oder Nexus sondern auch alltägliche Namen, Bezeichner und geografische Orte
- Achte darauf, den Ort in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
- Generiere auch Orte, die für die breite Masse der Bevölkerung und nicht nur für Runner geeignet ist
- Beachte die geänderte Weltordnung, Länder und Regionen der Sechsten Welt von Shadowrun, wie: ADL, CAS, CFS, Japanisches Kaiserreich, Tír na nÓg, Tír Tairngire oder UCAS
- Relevante Gebiete sind unter anderem, aber nicht ausschließlich, Seattle, Chicago, Los Angeles, London, Hamburg, Paris, Berlin, Hong Kong, Neo-Tokyo
- Gilden gibt es nicht mehr
- Wachgeister gibt es nicht
- Magische Sicherheit gibt es nur in Sicherheitstechnisch gehobenen Locations
- Die Bewertungen sollen ähnlich von Google Bewertungen von Google Maps sein
- Antworte als JSON, nur mit strings, mit Ausnahme von "Bewertungen" wo eine Liste von Objects zurückkommt in der Form: 
{
   'name': '', // Name der Person
   'rating': 1 // 1 bis 5
   'comment': '' // Kommentar der Person über die Location. Kann lustig, böse, zynisch und einfach dumm sein.
    
}
- Es sollen 5 Bewertungen generiert werden
"""

    def json_format(self):
        return json.dumps(
            {
                (attr.name, attr.additional_data)
                for attr in self.entity.ATTRIBUTE_DEFINITION
            }
        )

    def interpret_result(self, success):
        values = json.loads(success.data)

        self.entity.add_values(values)
        return success
