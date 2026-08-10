import json
from enum import Enum

from npc_creator import config
from npc_creator.models import Entity


def entity_prompt(entity, schema_name, filled_values):
    result = ""
    values = entity.values

    schema = entity.SCHEMAS[schema_name]
    for name, attribute in schema.__fields__.items():
        comment = ""
        if attribute.description:
            comment = f" // {attribute.description}"

        if (name in values and filled_values) or (
            name not in values and not filled_values
        ):
            value_or_type = values.get(name, None)
            if value_or_type is None:
                if issubclass(attribute.annotation, Enum):
                    value_or_type = ""
                else:
                    value_or_type = attribute.annotation()

            result += f"'{name}': {json.dumps(value_or_type)}{comment}\n"

    return f"{{\n{result}\n}}"

