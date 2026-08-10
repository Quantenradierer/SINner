from copy import deepcopy
from itertools import product
import json
import logging
import os
import os.path
from collections.abc import Iterable

from pydantic import ValidationError

from npc_creator.game_mechanics.sr6.rule import Rule
from npc_creator.game_mechanics.sr6.gear_collection import GearCollection

from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.manager import ALL_GEAR, ALL_RULES
from shadowrun.settings import BASE_DIR


def gear_files() -> Iterable[str]:
    for root, dirs, files in os.walk(
        os.path.join(BASE_DIR, "data", "sr6", "core", "gear")
    ):
        paths = [
            os.path.join(root, filename)
            for filename in files
            if filename.endswith(".json")
        ]
        yield from paths


def recursively_format(value, combination_with_keys):
    if isinstance(value, str):
        return value.format_map(combination_with_keys)
    elif isinstance(value, list):
        return [recursively_format(item, combination_with_keys) for item in value]
    elif isinstance(value, dict):
        return {
            key: recursively_format(value, combination_with_keys)
            for key, value in value.items()
        }
    else:
        return value


def extend_multi_parameter_definition(org_definition) -> list:
    if "parameter" in org_definition:
        parameter = org_definition.pop("parameter")
        keys = list(parameter.keys())
        values = [parameter[key] for key in keys]
        for combination in product(*values):
            definition = deepcopy(org_definition)
            combination_with_keys = dict(zip(keys, combination))

            definition = recursively_format(definition, combination_with_keys)
            yield definition
    else:
        yield org_definition


def _load_gear():
    for path in gear_files():
        with open(path, encoding="utf-8") as file:
            logging.info("Loading %s", path)
            for org_definition in json.load(file):
                definitions = extend_multi_parameter_definition(org_definition)

                for definition in definitions:
                    try:
                        ALL_GEAR.add(
                            Gear.model_validate(
                                {"gear": GearCollection(), **definition}
                            )
                        )
                    except ValidationError:
                        logging.error(f"Definition is not valid: {definition}")
                        raise


def rule_files() -> Iterable[str]:
    for root, dirs, files in os.walk(
        os.path.join(BASE_DIR, "data", "sr6", "core", "rules")
    ):
        paths = [
            os.path.join(root, filename)
            for filename in files
            if filename.endswith(".json")
        ]
        yield from paths


def _load_rules() -> None:
    for path in rule_files():
        with open(path, encoding="utf-8") as file:
            logging.info("Loading %s", path)

            for org_definition in json.load(file):  # pyright: ignore [reportAny]
                definitions = extend_multi_parameter_definition(org_definition)

                for definition in definitions:
                    try:
                        ALL_RULES.add(Rule.model_validate(definition))
                    except ValidationError:
                        logging.error(f"Definition is not valid: {definition}")
                        raise


def startup():
    _load_rules()
    _load_gear()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    startup()

    print(ALL_GEAR)
    print(ALL_RULES)
