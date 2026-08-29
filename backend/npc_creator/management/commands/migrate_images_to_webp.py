"""Backfill stored WebP files for Image rows written before the switch to
Django-managed storage.

For every Image without a ``file``, this looks for the legacy PNG at
``<PUBLIC_IMAGE_PATH>/<plural-kind>/<name>.png``, converts it to WebP, and
stores it (plus a thumbnail) through the configured storage backend.

Safe to run repeatedly: rows that already have a ``file`` are skipped.

    python manage.py migrate_images_to_webp [--limit N] [--dry-run] [--delete-source]
"""

import os

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from npc_creator.models.image import Image
from npc_creator.services.image_generation.store_image import encode_webp, THUMBNAIL_SIZE
from npc_creator.utils import entity_directory


class Command(BaseCommand):
    help = "Convert legacy on-disk PNGs to stored WebP files."

    def add_arguments(self, parser):
        parser.add_argument("--limit", type=int, default=0, help="process at most N images")
        parser.add_argument("--dry-run", action="store_true", help="report only, write nothing")
        parser.add_argument(
            "--delete-source",
            action="store_true",
            help="remove the legacy .png (and jpgs/ thumbnail) after a successful convert",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        limit = options["limit"]

        pending = Image.objects.filter(file="").select_related("entity").order_by("id")
        total = pending.count()
        self.stdout.write(f"{total} image(s) without a stored file")

        done = skipped = missing = 0
        for image in pending.iterator():
            if limit and done >= limit:
                break

            if not image.entity_id:
                skipped += 1
                continue

            legacy = os.path.join(entity_directory(image.entity.kind), f"{image.name}.png")
            if not os.path.isfile(legacy):
                self.stderr.write(f"  missing source: {legacy}")
                missing += 1
                continue

            if dry_run:
                self.stdout.write(f"  would convert {legacy}")
                done += 1
                continue

            with open(legacy, "rb") as fh:
                raw = fh.read()

            stem = image.name
            image.file.save(f"{stem}.webp", ContentFile(encode_webp(raw)), save=False)
            image.thumbnail.save(
                f"{stem}.thumb.webp",
                ContentFile(encode_webp(raw, THUMBNAIL_SIZE)),
                save=False,
            )
            image.save(update_fields=["file", "thumbnail"])
            done += 1

            if options["delete_source"]:
                for path in (
                    legacy,
                    os.path.join(entity_directory(image.entity.kind), "jpgs", f"{image.name}.jpg"),
                ):
                    try:
                        os.remove(path)
                    except FileNotFoundError:
                        pass

            if done % 100 == 0:
                self.stdout.write(f"  ...{done}")

        self.stdout.write(
            self.style.SUCCESS(
                f"converted={done} skipped={skipped} missing_source={missing}"
            )
        )
