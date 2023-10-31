from npc_creator import config
from npc_creator.operations.gpt.fill_npc import FillNpc

from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.services.interpret_gpt import dict_from_text


class CheckNpc(FillNpc):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = "- Antworte NUR mit 'Ok' oder mit einer Erklärung warum der NPC abgelehnt wurde \n- Die Attribute sollten einen NPC einen Shadowrun darstellen\n- Prüf ob die Daten inhaltlich passen\n- Verwirf Urheberrechtsverletzungen oder zu extreme Namen oder Beschreibungen\n- Der NPC sollte eine gewisse Qualität haben"
        self.gpt = GptInterface.GptVersion.GPT4

    def interpret_result(self, success):
        attributes = dict_from_text(config.RELEVANT_ATTRIBUTES, success.data)

        if not attributes:
            empty_attribute = self.get_empty_attribute()
            if empty_attribute:
                attributes = {empty_attribute: success.data}

        self.npc.add_attributes(attributes)
        return success
