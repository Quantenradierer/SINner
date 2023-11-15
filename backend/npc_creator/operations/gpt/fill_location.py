from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.services.interpret_gpt import dict_from_text


class FillLocation(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """- Vervollständige eine Location für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Achte darauf, den NPC in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
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

        self.entity.add_values(attributes)
        return success
