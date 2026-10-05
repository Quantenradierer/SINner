"""Validate a floorplan request against SINner's hard caps.

roomplanner is imported lazily so the rest of the app still runs where it is not installed.
"""

from dataclasses import dataclass
from typing import Any

# Selectable image themes: public name -> roomplanner theme.
THEMES = {"neon2": "neon2_sprites", "modern2": "modern2_sprites"}
DEFAULT_THEME = "neon2"

MIN_SIDE_CELLS = 8
MAX_SIDE_CELLS = 120  # 60 m
MAX_FLOORS_ABOVE = 6
MAX_FLOORS_BELOW = 2
# Fixed image quality; not chosen per request.
CELL_PX = 25
SUPERSAMPLE = 1
SEED_RANGE = 2**31

# Image pixels around the building; the page's overlays rely on it.
PADDING = 2


class RequestError(ValueError):
    """The request is malformed or exceeds a cap (HTTP 400)."""


@dataclass(frozen=True)
class FloorplanRequest:
    params: Any  # roomplanner.params.GenerationParams
    theme: str  # key of THEMES

    def as_attributes(self) -> dict[str, Any]:
        """JSON stored on the entity; feeds the gallery search and the detail page."""
        return {
            "params": self.params.model_dump(mode="json"),
            "theme": self.theme,
            "name": f"{self.params.building_type.value} "
            f"{self.params.width}x{self.params.depth}",
        }


def _int(raw: dict[str, Any], key: str, low: int, high: int) -> int:
    value = raw.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise RequestError(f"{key} must be an integer")
    if not low <= value <= high:
        raise RequestError(f"{key} must be {low}..{high}")
    return value


def parse_request(data: object) -> FloorplanRequest:
    from pydantic import ValidationError
    from roomplanner.params import GenerationParams

    if not isinstance(data, dict):
        raise RequestError("expected a JSON object")
    raw = data.get("params")
    if not isinstance(raw, dict):
        raise RequestError("missing params")

    raw = dict(raw)
    raw.pop("room", None)  # a single room is a debugging mode; always the whole building
    # Generation is deterministic per seed; pin it so the stored request reproduces.
    if raw.get("seed") is None:
        import secrets

        raw["seed"] = secrets.randbelow(SEED_RANGE)
    _int(raw, "width", MIN_SIDE_CELLS, MAX_SIDE_CELLS)
    _int(raw, "depth", MIN_SIDE_CELLS, MAX_SIDE_CELLS)
    _int(raw, "seed", 0, SEED_RANGE)
    if "floors_above" in raw:
        _int(raw, "floors_above", 1, MAX_FLOORS_ABOVE)
    if "floors_below" in raw:
        _int(raw, "floors_below", 0, MAX_FLOORS_BELOW)

    try:
        params = GenerationParams.model_validate(raw)
    except ValidationError as error:
        raise RequestError(
            "; ".join(
                f"{'.'.join(str(p) for p in e['loc']) or 'params'}: {e['msg']}"
                for e in error.errors()
            )
        ) from error

    theme = data.get("theme", DEFAULT_THEME)
    if theme not in THEMES:
        raise RequestError(f"theme must be one of {', '.join(THEMES)}")
    return FloorplanRequest(params=params, theme=theme)


def options() -> dict[str, Any]:
    """Choices and caps for the form."""
    from roomplanner.geometry import Side
    from roomplanner.params import (
        BuildingType,
        Condition,
        Security,
        Shape,
        Wealth,
    )

    return {
        "building_types": [t.value for t in BuildingType],
        "wealth": [w.value for w in Wealth],
        "condition": [c.value for c in Condition],
        "security": [s.value for s in Security],
        "shape": [s.value for s in Shape],
        "sides": [s.value for s in Side],
        "themes": list(THEMES),
        "limits": {
            "side_cells": [MIN_SIDE_CELLS, MAX_SIDE_CELLS],
            "floors_above": [1, MAX_FLOORS_ABOVE],
            "floors_below": [0, MAX_FLOORS_BELOW],
            "seed": [0, SEED_RANGE],
        },
        "defaults": {"theme": DEFAULT_THEME},
    }
