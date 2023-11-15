
from npc_creator.models.entities.location import Location
from npc_creator.models.gpt_request import GptRequest
from npc_creator.operations import GenerateLocation
from npc_creator.operations.return_types import Success


from django.test import TestCase


class GenerateLocationTest(TestCase):
    def test_generate_location_success(self):
        # Given
        entity = Location()
        fill_location_result = Success(data=entity)
        generate_loc = GenerateLocation(user_prompt='Erzeuge eine Bar', entity=entity)
        result = generate_loc.call()
        assert isinstance(result, Success)
        assert result.data == entity
