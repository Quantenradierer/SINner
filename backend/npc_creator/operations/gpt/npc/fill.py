from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.services.interpret_gpt import dict_from_text
from npc_creator.operations.gpt import entity


class Fill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """- Vervollständige einen NPC für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Erstelle unangemessene, extreme, rassistische oder homophobe NPC so, das du zeigst wie falsch ihre Werte sind 
- Erstelle keine Urheberrechtlich geschützten Figuren oder Personen
- Erstelle keine Runner oder Söldner, sofern nicht anders gewünscht
- Das Geheimnis muss detailliert beschrieben sein
- Der Name ist in der Form 'Vorname "Rufname" Nachname' 
- Sei beim Namen kreativ
- Nutze seltene und unübliche Namen 
- Achte darauf, den NPC in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
- Zwerge sind keine Schmiede oder Braumeister, sondern gehen reguläre Berufe der Modernen Zeit nach
- Elfen sind maximal 70 Jahre alt
- Erstelle standardmäßig weniger Personen mit afro-Ethnizität
- Beachte die geänderte Weltordnung, Länder und Regionen der Sechsten Welt von Shadowrun, wie: ADL, CAS, CFS, Japanisches Kaiserreich, Tír na nÓg, Tír Tairngire oder UCAS
"""

    @property
    def entity(self):
        return self.kwargs["entity"]

    @property
    def user_prompt(self):
        return self.kwargs.get("user_prompt", "")

    def prompt(self):
        return [
            self.user_prompt,
        ] + entity_prompt(self.entity)

    def get_empty_attribute(self):
        """
        Returns: the empty attribute, if there is only one, or None otherwise
        """
        for key, value in self.entity.primary_values.items():
            if not value.strip():
                return key

    def interpret_result(self, success):
        names = self.entity.attribute_names
        attributes = dict_from_text(names, success.data)

        if not attributes:
            empty_attribute = self.get_empty_attribute()
            if empty_attribute:
                attributes = {empty_attribute: success.data}

        attributes = self._clean_result(attributes)
        self.entity.add_values(attributes)
        return success

    def _clean_result(self, attributes):
        for attr in self.entity.ATTRIBUTE_DEFINITION:
            if attr.name in attributes and attr.length:
                attributes[attr.name] = attributes[attr.name][: attr.length].strip()

        return attributes
