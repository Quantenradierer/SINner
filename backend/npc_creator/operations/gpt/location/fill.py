import json

from npc_creator.operations.gpt import entity


class Fill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_json = True
        self.system_prompt = """- Vervollständige eine Location für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Sei beim Namen kreativ, nicht nur Neon oder Nexus sondern auch alltägliche Namen, Bezeichner und geografische Orte
- Achte darauf, den Ort in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
- Generiere auch Orte, die für die breite Masse der Bevölkerung und nicht nur für Runner geeignet ist
- Beachte die geänderte Weltordnung, Länder und Regionen der Sechsten Welt von Shadowrun, wie: ADL, CAS, CFS, Japanisches Kaiserreich, Tír na nÓg, Tír Tairngire oder UCAS
- Relevante Gebiete sind unter anderem, aber nicht ausschließlich, Seattle, Chicago, Los Angeles, London, Hamburg, Paris, Berlin, Hong Kong, Neo-Tokyo
- Gilden gibt es nicht mehr
- Wachgeister gibt es nicht
- Magische Sicherheit gibt es nur in Sicherheitstechnisch gehobenen Locations
- Die Bewertungen sollen ähnlich von Google Bewertungen von Google Maps sein
- Aussehen soll als {'Aussehen': string} angegeben werden 
- Antworte als JSON, immer als {key: string} Format, mit Ausnahme von "Bewertungen" wo eine Liste von Objects zurückkommt in der Form: 
{
   'name': '', // Name der Person
   'rating': 1 // 1 bis 5
   'comment': '' // Kommentar der Person über die Location. Kann lustig, böse, zynisch und einfach dumm sein.
    
}
- Es sollen 5 Bewertungen generiert werden
"""

    def interpret_result(self, success):
        values = success.data
        if "innen" in values["Aussehen"] and isinstance(
            values["Aussehen"]["innen"], dict
        ):
            values["Aussehen"] = values["Aussehen"]["innen"]

        self.entity.add_values(values)
        return success
