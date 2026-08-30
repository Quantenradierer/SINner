"""Human-readable names for SR6 reference data (gear + rules), keyed by id.

The lookup table ships with the package at
``reference/sr6/core/i18n/<lang>.json`` (see game_mechanics.startup for the
reference-data layout). Entries are best-effort German names taken from the
SR6 Grundregelwerk; regenerate the file when the reference data changes.
"""

import json
import logging
import os
from functools import cache

from npc_creator import config

I18N_DIR = os.path.join(config.REFERENCE_DIR, "sr6", "core", "i18n")
DEFAULT_LANG = "de"


@cache
def _names(lang: str) -> dict[str, str]:
    path = os.path.join(I18N_DIR, f"{lang}.json")
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except OSError as exc:
        logging.warning("reference name table %s unavailable (%s)", path, exc)
        return {}


def name_for(gear_id: str, lang: str = DEFAULT_LANG) -> str:
    """Return the display name for a gear/rule id, or the id itself if unknown."""
    return _names(lang).get(gear_id, gear_id)


def resolve_equipment(equipment, lang: str = DEFAULT_LANG) -> list[dict]:
    """Normalise a stored ``equipment`` value into ``[{"id", "name"}, ...]``.

    Accepts the legacy comma-separated string, a list of id strings, or a list
    of ``{"id": ..., "mods": [...]}`` objects.
    """
    if not equipment:
        return []

    if isinstance(equipment, str):
        items = [part.strip() for part in equipment.split(",") if part.strip()]
    elif isinstance(equipment, list):
        items = []
        for entry in equipment:
            if isinstance(entry, str):
                items.append(entry)
            elif isinstance(entry, dict) and entry.get("id"):
                items.append(entry["id"])
    else:
        return []

    return [{"id": item, "name": name_for(item, lang)} for item in items]
