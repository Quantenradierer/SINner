"""Generate a building with roomplanner and persist its images and files."""

import io
import uuid
from typing import Callable

from django.core.files.base import ContentFile

from npc_creator.models import Entity
from npc_creator.models.floorplan import FloorplanFile
from npc_creator.services.floorplan.request import (
    CELL_PX,
    PADDING,
    SUPERSAMPLE,
    THEMES,
    FloorplanRequest,
)
from npc_creator.services.image_generation.store_image import store_entity_image

Progress = Callable[[int, int], None]


def render_floorplan(
    entity: Entity, request: FloorplanRequest, progress: Progress
) -> None:
    """Raises roomplanner.errors.RoomplannerError for buildings that can't be generated.

    Per floor one gallery image (the page's overlays are drawn on it, hence the padding)
    and one dd2vtt file, plus the building JSON for the overlays. Steps: generate,
    then render + export per floor.
    """
    from roomplanner.export.common import ExportOptions
    from roomplanner.export.uvtt import uvtt_json
    from roomplanner.generator import generate
    from roomplanner.i18n import Language
    from roomplanner.render.image import RenderOptions, render_floor
    from roomplanner.render.theme import load_theme
    from roomplanner.serialization import to_json

    theme = load_theme(THEMES[request.theme])
    steps_total = 1 + len(request.params.levels)
    progress(0, steps_total)

    building = generate(request.params)
    progress(1, steps_total)

    language = Language(request.language)
    options = RenderOptions(
        CELL_PX,
        padding=PADDING,
        lighting=True,
        supersample=SUPERSAMPLE,
        language=language,
    )
    export_options = ExportOptions(cell_px=CELL_PX, language=language)
    for done, floor in enumerate(building.floors, start=2):
        picture = render_floor(building, floor, theme, options)
        buffer = io.BytesIO()
        picture.save(buffer, "PNG", compress_level=1)
        store_entity_image(buffer.getvalue(), entity)
        _store_file(
            entity,
            FloorplanFile.Kind.DD2VTT,
            floor.level,
            uvtt_json(building, floor, theme, export_options),
            "dd2vtt",
        )
        progress(done, steps_total)

    _store_file(entity, FloorplanFile.Kind.BUILDING, None, to_json(building), "json")
    entity.attributes = {
        **entity.attributes,
        "levels": [floor.level for floor in building.floors],
        "warnings": list(building.warnings),
    }
    entity.save()


def _store_file(
    entity: Entity, kind: str, level: int | None, text: str, extension: str
) -> None:
    record = FloorplanFile(entity=entity, kind=kind, level=level)
    record.file.save(
        f"{uuid.uuid1()}.{extension}", ContentFile(text.encode("utf-8")), save=False
    )
    record.save()
