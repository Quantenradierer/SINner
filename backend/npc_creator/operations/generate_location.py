from npc_creator.models.entity import Entity
from npc_creator.operations.gpt.fill_location import FillLocation
from npc_creator.operations.gpt.fill_npc import FillNpc
from npc_creator.operations.return_types import Failure, Success


class GenerateLocation:
    def __init__(self, user_prompt: str = "", entity: Entity = None):
        self.entity = entity or Entity()
        self.user_prompt = user_prompt

    def call(self):
        result = FillLocation(entity=self.entity, user_prompt=self.user_prompt).call()
        if result:
            return Success(data=self.entity)
        return Failure(error=result.error)
