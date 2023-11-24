from npc_creator.operations.gpt import entity


class Check(entity.Check):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = "- Antworte NUR mit 'Ok' oder mit einer Erklärung warum der NPC abgelehnt wurde \n- Die Attribute sollten einen NPC einen Shadowrun darstellen\n- Prüf ob die Daten inhaltlich passen\n- Verwirf Urheberrechtsverletzungen oder zu extreme Namen oder Beschreibungen\n- Der NPC sollte eine gewisse Qualität haben"
