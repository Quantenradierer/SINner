from npc_creator import config
from npc_creator.models import Npc

from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import npc_prompt
from npc_creator.services.interpret_gpt import dict_from_text


class FillNpc(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """- Vervollständige einen NPC für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Erstelle unangemessene, extreme, rassistische oder homophob+e NPC so, das du zeigst wie falsch ihre Werte sind 
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
    def npc(self):
        return self.kwargs['npc']

    @property
    def user_prompt(self):
        return self.kwargs.get('user_prompt', '')

    def prompt(self):
        return [self.user_prompt, ] + npc_prompt(self.npc)

    def get_empty_attribute(self):
        '''
        Returns: the empty attribute, if there is only one, or None otherwise
        '''
        for key, value in self.npc.attributes.items():
            if not value.strip():
                return key

    def interpret_result(self, success):
        names = [attr_def.name for attr_def in Npc.ATTRIBUTE_DEFINITION]
        attributes = dict_from_text(names, success.data)

        if not attributes:
            empty_attribute = self.get_empty_attribute()
            if empty_attribute:
                attributes = {empty_attribute: success.data}

        self.npc.add_attributes(attributes)
        return success