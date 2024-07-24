import json

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
            result += f"'{name}': {json.dumps(values.get(name, ''))}{comment}\n"

    return f"{{\n{result}\n}}"


# min([metadata.max_length for metadata in attribute.metadata])
