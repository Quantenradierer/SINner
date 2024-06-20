from npc_creator.operations.gpt import entity


class Check(entity.Check):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = (
            "- Antworte als JSON leeres object, wenn alles in Ordnung ist. Ansonsten beschreibe das Problem in der Form: {'attribute': 'problem'}"
            "- Prüf ob die Daten inhaltlich passen"
            "- Verwirf Urheberrechtsverletzungen oder zu extreme Namen oder Beschreibungen"
            "- Es sollte eine gewisse Qualität haben"
        )
