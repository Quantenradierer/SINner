from npc_creator import config

from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.services.interpret_gpt import dict_from_text


class FillNpc(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT3_5
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
        """
        Function to create a prompt for a non-player character (NPC) using the given attributes.
        The result will be in three parts: the user prompt itself, the current attributes and the missing attributes

        Parameters
        ----------
        user_prompt : str
            The user prompt text.
        npc_attributes : Dict[str, str]
            A dictionary containing the NPC's attributes.
        relevant_attributes : List[str]
            A list containing the all attributes to be considered.

        Returns
        -------
        List
            A list containing the user prompt, npc attributes, and other attributes.

        Examples
        --------
        >>> create_npc_prompt("Create a NPC", {"name": "John", "age": "30"}, ["name", "job", "age", "height"])
        ["Create a NPC", {"name": "John", "age": "30"}, {"job": "", "height": ""}]
        """
        npc_attributes = self.npc.attributes
        relevant_attributes = config.RELEVANT_ATTRIBUTES

        npc_attributes_filtered = dict([(key, value) for key, value in npc_attributes.items() if value])
        attributes_filtered = dict([(key, "") for key in relevant_attributes if key not in npc_attributes_filtered])

        prompt_parts = [self.user_prompt, npc_attributes_filtered, attributes_filtered]

        formatted_prompts = []
        for prompt in prompt_parts:
            if type(prompt) is not str:
                prompt = '\n'.join([f'{key}: {value}' for key, value in prompt.items()])
            formatted_prompts.append(prompt)
        return formatted_prompts

    def get_empty_attribute(self):
        '''
        Returns: the empty attribute, if there is only one, or None otherwise
        '''
        for key, value in self.npc.attributes.items():
            if not value.strip():
                return key

    def interpret_result(self, success):
        attributes = dict_from_text(config.RELEVANT_ATTRIBUTES, success.data)

        if not attributes:
            empty_attribute = self.get_empty_attribute()
            if empty_attribute:
                attributes = {empty_attribute: success.data}

        self.npc.add_attributes(attributes)
        return success
