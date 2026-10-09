import json

from npc_creator.operations.gpt import entity


ENGLISH_PROMPT = """- Complete a location for a Shadowrun pen & paper roleplaying game
- If no information is given, make some up
- Be creative with the name, not only Neon or Nexus but also everyday names, designations and geographic places
- Integrate the place into the Shadowrun world and make it appealing for the players
- Also generate places suitable for the general population, not only for runners
- Respect the changed world order, countries and regions of the Sixth World of Shadowrun, such as: ADL, CAS, CFS, Japanese Imperial State, Tír na nÓg, Tír Tairngire or UCAS
- Relevant areas include, but are not limited to, Seattle, Chicago, Los Angeles, London, Hamburg, Paris, Berlin, Hong Kong, Neo-Tokyo
- Guilds no longer exist
- Watcher spirits do not exist
- Magical security only exists in locations with elevated security
- The reviews should be similar to Google reviews on Google Maps
- Answer in English. Every text value must be English, whatever language the input is in
- Answer as JSON, always in {key: string} format, except for "reviews", which is a list of objects of the form:
{
   'name': '', // name of the reviewer
   'rating': 1 // 1 to 5
   'comment': '' // the reviewer's comment about the location. Can be funny, mean, cynical or just stupid.
}
- Generate 5 reviews
"""


class Fill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        if self.entity.language == self.entity.Languages.ENGLISH:
            self.system_prompt = ENGLISH_PROMPT
