from npc_creator.operations.gpt import entity


class Check(entity.Check):
    def call(self):
        return True
