import logging
from threading import Thread

from npc_creator.models.entity import Entity
from npc_creator.models.floorplan import FloorplanGeneration
from npc_creator.services.floorplan.render import render_floorplan
from npc_creator.services.floorplan.request import parse_request


def floorplan_job(generation_id: int) -> None:
    """Thread entry point: whatever goes wrong ends as FAILED with a message, so the
    polling page stops and shows it."""
    generation = FloorplanGeneration.objects.select_related("entity").get(
        pk=generation_id
    )
    generation.state = FloorplanGeneration.State.RENDERING
    generation.save(update_fields=["state", "updated_at"])

    def progress(done: int, total: int) -> None:
        FloorplanGeneration.objects.filter(pk=generation_id).update(
            steps_done=done, steps_total=total
        )

    try:
        entity = Entity.objects.get(pk=generation.entity_id)
        request = parse_request(entity.attributes)
        render_floorplan(entity, request, progress)
    except Exception as error:
        logging.exception(f"FloorplanJob({generation_id}): failed")
        FloorplanGeneration.objects.filter(pk=generation_id).update(
            state=FloorplanGeneration.State.FAILED, error=_message(error)
        )
        return
    FloorplanGeneration.objects.filter(pk=generation_id).update(
        state=FloorplanGeneration.State.DONE
    )


def _message(error: Exception) -> str:
    """Roomplanner explains impossible inputs; anything else stays in the log."""
    try:
        from roomplanner.errors import RoomplannerError
    except ImportError:
        return "Floorplan generation is not available."
    if isinstance(error, RoomplannerError):
        return str(error)
    return "Floorplan generation failed."


def floorplan_job_async(generation: FloorplanGeneration) -> None:
    Thread(target=floorplan_job, args=[generation.id], daemon=True).start()
