import json

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from npc_creator.jobs.floorplan_job import floorplan_job_async
from npc_creator.models import Entity
from npc_creator.models.entities.floorplan import Floorplan
from npc_creator.models.floorplan import FloorplanFile, FloorplanGeneration
from npc_creator.services.floorplan.request import (
    DEFAULT_LANGUAGE,
    LANGUAGES,
    PADDING,
    RequestError,
    options,
    parse_request,
)


def _error(message: str, code: int) -> Response:
    return Response({"type": "error", "error": message}, status=code)


class FloorplanViewSet(viewsets.ViewSet):
    """Floorplans are immutable: `create` makes a new one, `publish` is the only change.

    Creating returns at once; the page polls `status` while a background thread renders.
    """

    permission_classes = []
    lookup_field = "pk"

    def _floorplan(self, pk) -> Floorplan:
        return get_object_or_404(Floorplan.objects, uuid=pk)

    @action(detail=False, methods=["get"])
    def options(self, request):
        try:
            language = request.query_params.get("lang", DEFAULT_LANGUAGE)
            return Response(
                options(language if language in LANGUAGES else DEFAULT_LANGUAGE)
            )
        except ImportError:
            return _error(
                "Floorplan generation is not installed.",
                status.HTTP_503_SERVICE_UNAVAILABLE,
            )

    def create(self, request):
        try:
            data = json.loads(request.body.decode())
            floorplan_request = parse_request(data)
        except (RequestError, json.JSONDecodeError) as error:
            return _error(str(error), status.HTTP_400_BAD_REQUEST)
        except ImportError:
            return _error(
                "Floorplan generation is not installed.",
                status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        attributes = floorplan_request.as_attributes()
        existing = _existing(attributes)
        if existing:
            return Response(
                {
                    "type": "success",
                    "id": existing.uuid,
                    "status": _status(_generation(existing)),
                    "existing": True,
                },
                status=status.HTTP_200_OK,
            )

        floorplan = Floorplan(
            attributes=attributes,
            language=floorplan_request.language,
        )
        if request.user.is_authenticated:
            floorplan.creator = request.user
        with transaction.atomic():
            floorplan.save()
            generation = FloorplanGeneration.objects.create(entity=floorplan)
        # After the commit, or the thread may not find the rows.
        floorplan_job_async(generation)
        return Response(
            {"type": "success", "id": floorplan.uuid, "status": _status(generation)},
            status=status.HTTP_201_CREATED,
        )

    def retrieve(self, request, pk=None):
        floorplan = self._floorplan(pk)
        generation = _generation(floorplan)
        return Response(
            {
                "id": floorplan.uuid,
                "state": floorplan.state,
                "attributes": floorplan.attributes,
                "status": _status(generation),
                "padding": PADDING,
                "building_url": _building_url(floorplan),
                "floors": _floors(floorplan),
            }
        )

    @action(detail=True, methods=["get"])
    def status(self, request, pk=None):
        return Response(_status(_generation(self._floorplan(pk))))

    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        floorplan = self._floorplan(pk)
        if floorplan.creator_id not in (None, request.user.pk):
            return _error("Not your floorplan.", status.HTTP_403_FORBIDDEN)
        if _generation(floorplan).state != FloorplanGeneration.State.DONE:
            return _error("The floorplan is not finished.", status.HTTP_409_CONFLICT)
        if floorplan.state != Entity.States.UNPUBLISHED:
            return _error(
                "This entity is already published and can no longer be edited.",
                status.HTTP_403_FORBIDDEN,
            )
        floorplan.state = Entity.States.PUBLISHED
        floorplan.save(update_fields=["state", "updated_at"])
        return Response({"type": "success", "state": floorplan.state})


def _existing(attributes: dict) -> Floorplan | None:
    """A floorplan made from the same parameters (generation is deterministic per seed),
    unless its rendering failed."""
    wanted = {key: attributes[key] for key in ("params", "theme", "language")}
    candidates = Floorplan.objects.filter(
        attributes__params__seed=attributes["params"]["seed"],
        floorplan_generation__state__in=[
            FloorplanGeneration.State.DONE,
            FloorplanGeneration.State.QUEUED,
            FloorplanGeneration.State.RENDERING,
        ],
    ).order_by("id")
    for candidate in candidates:
        if all(candidate.attributes.get(key) == value for key, value in wanted.items()):
            return candidate
    return None


def _generation(floorplan: Floorplan) -> FloorplanGeneration:
    return get_object_or_404(FloorplanGeneration.objects, entity_id=floorplan.pk)


def _status(generation: FloorplanGeneration) -> dict:
    return {
        "state": generation.state,
        "steps_done": generation.steps_done,
        "steps_total": generation.steps_total,
        "error": generation.error,
    }


def _building_url(floorplan: Floorplan) -> str | None:
    record = floorplan.floorplan_files.filter(kind=FloorplanFile.Kind.BUILDING).first()
    return record.file.url if record else None


def _floors(floorplan: Floorplan) -> list[dict]:
    """Per floor: gallery image and dd2vtt, both created in level order."""
    images = list(floorplan.image_set.order_by("id"))
    vtt = {
        record.level: record.file.url
        for record in floorplan.floorplan_files.filter(kind=FloorplanFile.Kind.DD2VTT)
    }
    levels = floorplan.attributes.get("levels", [])
    return [
        {
            "level": level,
            "image_url": image.file_url,
            "thumbnail_url": image.thumbnail_url,
            "dd2vtt_url": vtt.get(level),
        }
        for level, image in zip(levels, images)
    ]
