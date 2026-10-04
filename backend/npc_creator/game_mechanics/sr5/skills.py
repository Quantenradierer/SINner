"""Active skills of the Shadowrun 5 core rulebook (p. 130-151), by category."""

SKILLS_BY_CATEGORY = {
    "combat": [
        "Archery", "Automatics", "Blades", "Clubs", "Exotic Melee Weapon", "Exotic Ranged Weapon",
        "Heavy Weapons", "Longarms", "Pistols", "Throwing Weapons", "Unarmed Combat", "Gunnery",
    ],
    "physical": [
        "Disguise", "Diving", "Escape Artist", "Free-Fall", "Gymnastics", "Locksmith", "Palming",
        "Perception", "Running", "Sneaking", "Survival", "Swimming", "Tracking",
    ],
    "social": [
        "Animal Handling", "Con", "Etiquette", "Impersonation", "Instruction", "Intimidation",
        "Leadership", "Negotiation", "Performance",
    ],
    "magical": [
        "Alchemy", "Arcana", "Artificing", "Assensing", "Astral Combat", "Banishing", "Binding",
        "Counterspelling", "Disenchanting", "Ritual Spellcasting", "Spellcasting", "Summoning",
    ],
    "resonance": ["Compiling", "Decompiling", "Registering"],
    "technical": [
        "Aeronautics Mechanic", "Armorer", "Artisan", "Automotive Mechanic", "Biotechnology", "Chemistry",
        "Computer", "Cybercombat", "Cybertechnology", "Demolitions", "Electronic Warfare", "First Aid",
        "Forgery", "Hacking", "Hardware", "Industrial Mechanic", "Medicine", "Nautical Mechanic",
        "Navigation", "Software",
    ],
    "vehicle": [
        "Pilot Aerospace", "Pilot Aircraft", "Pilot Exotic Vehicle", "Pilot Ground Craft", "Pilot Walker",
        "Pilot Watercraft",
    ],
}

EXOTIC = ("Exotic Melee Weapon", "Exotic Ranged Weapon", "Pilot Exotic Vehicle")


def skill_key(name: str) -> str:
    return "sr5_skill_" + name.lower().replace("-", "_").replace(" ", "_")


SKILL_NAMES = {skill_key(name): name for names in SKILLS_BY_CATEGORY.values() for name in names}
MAGICAL_KEYS = [skill_key(name) for name in SKILLS_BY_CATEGORY["magical"]]
RESONANCE_KEYS = [skill_key(name) for name in SKILLS_BY_CATEGORY["resonance"]]
