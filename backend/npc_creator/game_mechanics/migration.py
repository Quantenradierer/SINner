import json
import os

from npc_creator.game_mechanics.startup import gear_files, rule_files


if __name__ == "__main__":
    for file in rule_files():
        with open(file, "r") as handle:
            content = json.load(handle)

            for rule in content:
                rule["id"] = f'sr6core/{rule["id"].lower()}'

        with open(file, "w+") as handle:
            json.dump(content, handle, indent=2)
