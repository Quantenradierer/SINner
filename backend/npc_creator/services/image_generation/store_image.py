"""Single entry point for persisting a generated entity image.

Takes raw bytes (PNG from DALL-E / gpt-image, or a crop of a Midjourney grid),
converts to WebP, stores the full-size image and a resized thumbnail through
Django's storage backend, and returns the created ``Image`` row.
"""

import io
import uuid
from typing import Optional

from django.core.files.base import ContentFile
from PIL import Image as PILImage

from npc_creator.models.image import Image
from npc_creator.models.image_generation import ImageGeneration

WEBP_QUALITY = 80
THUMBNAIL_SIZE = (512, 512)


def encode_webp(data: bytes, max_size: Optional[tuple[int, int]] = None) -> bytes:
    im = PILImage.open(io.BytesIO(data))
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
    if max_size is not None:
        im.thumbnail(max_size)
    buffer = io.BytesIO()
    im.save(buffer, "WEBP", quality=WEBP_QUALITY, method=6)
    return buffer.getvalue()


def store_entity_image(
    image_bytes: bytes,
    entity,
    generation: Optional[ImageGeneration] = None,
) -> Image:
    stem = str(uuid.uuid1())
    image = Image(entity=entity, generation=generation, name=stem)
    image.file.save(
        f"{stem}.webp", ContentFile(encode_webp(image_bytes)), save=False
    )
    image.thumbnail.save(
        f"{stem}.thumb.webp",
        ContentFile(encode_webp(image_bytes, THUMBNAIL_SIZE)),
        save=False,
    )
    image.save()
    return image
