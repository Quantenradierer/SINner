from django.db import models
from npc_creator.models import Entity
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.utils import entity_directory, plural_entity_type


def entity_image_upload_to(instance: "Image", filename: str) -> str:
    """Shard uploads by the file stem so no directory holds more than a few
    hundred files: entities/<plural-kind>/<ab>/<cd>/<stem>[.thumb].webp
    """
    stem = filename.split(".")[0]
    kind = plural_entity_type(instance.entity.kind) if instance.entity_id else "unknown"
    return f"entities/{kind}/{stem[:2]}/{stem[2:4]}/{filename}"


class Image(models.Model):
    # Legacy uuid stem for rows written before the switch to stored files.
    name = models.CharField(max_length=255, blank=True)
    score = models.IntegerField(default=0)

    file = models.ImageField(upload_to=entity_image_upload_to, blank=True)
    thumbnail = models.ImageField(upload_to=entity_image_upload_to, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    generation = models.ForeignKey(
        ImageGeneration, null=True, on_delete=models.SET_NULL
    )
    entity = models.ForeignKey(Entity, null=True, on_delete=models.SET_NULL)

    def _legacy_url(self, thumbnail: bool = False) -> str:
        kind = plural_entity_type(self.entity.kind)
        if thumbnail:
            return f"/images/npc_creator/{kind}/jpgs/{self.name}.jpg"
        return f"/images/npc_creator/{kind}/{self.name}.png"

    @property
    def file_url(self) -> str:
        """Browser URL for the full-size image."""
        return self.file.url if self.file else self._legacy_url()

    @property
    def thumbnail_url(self) -> str:
        """Browser URL for the gallery-sized image."""
        if self.thumbnail:
            return self.thumbnail.url
        if self.file:
            return self.file.url
        return self._legacy_url(thumbnail=True)

    @property
    def url(self) -> str:
        """Filesystem path to the full-size image (used server-side, e.g. by
        the Foundry exporter)."""
        if self.file:
            return self.file.path
        return entity_directory(entity_kind=self.entity.kind) + "/" + self.name + ".png"

    @property
    def template(self):
        if self.generation:
            return self.generation.template

    def upvote(self):
        self.score += 1

    def downvote(self):
        self.score -= 1
