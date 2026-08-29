#!/usr/bin/env bash
# Consistent SQLite backup of the running sinner container.
#
# Safe to run while the app is live: it uses SQLite's online backup API, not a
# raw file copy. Keeps a local retention window and optionally pushes offsite
# with rclone.
#
# Config via environment (all optional):
#   SINNER_CONTAINER            container name           (default: sinner)
#   SINNER_BACKUP_DIR           where backups land       (default: /srv/backups/sinner)
#   SINNER_RETENTION_DAYS       prune db backups older   (default: 14)
#   SINNER_RCLONE_REMOTE        e.g. b2:bucket/sinner    (default: unset = skip)
#   SINNER_BACKUP_IMAGES        1 = also archive images  (default: 0)
#   SINNER_IMAGE_RETENTION_DAYS prune image archives     (default: 30)
#   SINNER_IMAGE                image for throwaway ops   (default: sinner:latest)
#   SINNER_VOLUME               data volume name         (default: sinner-data)
set -euo pipefail

CONTAINER="${SINNER_CONTAINER:-sinner}"
BACKUP_DIR="${SINNER_BACKUP_DIR:-/srv/backups/sinner}"
RETENTION_DAYS="${SINNER_RETENTION_DAYS:-14}"
RCLONE_REMOTE="${SINNER_RCLONE_REMOTE:-}"
IMAGE="${SINNER_IMAGE:-sinner:latest}"
VOLUME="${SINNER_VOLUME:-sinner-data}"

DB_IN_CONTAINER="/app/data/db.sqlite3"
TMP_IN_CONTAINER="/app/data/.backup.tmp.sqlite3"

command -v docker >/dev/null || { echo "error: docker not found" >&2; exit 1; }

if ! docker ps --format '{{.Names}}' | grep -qx "$CONTAINER"; then
    echo "error: container '$CONTAINER' is not running" >&2
    exit 1
fi

mkdir -p "$BACKUP_DIR"
ts="$(date +%Y-%m-%d_%H%M%S)"
dest="${BACKUP_DIR}/db_${ts}.sqlite3"

echo "==> creating consistent snapshot inside ${CONTAINER}"
docker exec -i -e DB="$DB_IN_CONTAINER" -e TMP="$TMP_IN_CONTAINER" \
    "$CONTAINER" python - <<'PY'
import os, sqlite3, sys

db, tmp = os.environ["DB"], os.environ["TMP"]
try:
    os.remove(tmp)
except FileNotFoundError:
    pass

src, dst = sqlite3.connect(db), sqlite3.connect(tmp)
with dst:
    src.backup(dst)
dst.close(); src.close()

result = sqlite3.connect(tmp).execute("PRAGMA integrity_check").fetchone()[0]
print("    integrity_check:", result)
sys.exit(0 if result == "ok" else 1)
PY

echo "==> copying out to ${dest}"
docker cp "${CONTAINER}:${TMP_IN_CONTAINER}" "$dest"
docker exec "$CONTAINER" rm -f "$TMP_IN_CONTAINER"
gzip -f "$dest"
dest="${dest}.gz"
echo "    $(du -h "$dest" | cut -f1)  ${dest}"

echo "==> pruning db backups older than ${RETENTION_DAYS} days"
find "$BACKUP_DIR" -maxdepth 1 -name 'db_*.sqlite3.gz' -mtime "+${RETENTION_DAYS}" -print -delete || true

if [ "${SINNER_BACKUP_IMAGES:-0}" = "1" ]; then
    echo "==> archiving generated images"
    docker run --rm -e TS="$ts" \
        -v "${VOLUME}:/app/data:ro" -v "${BACKUP_DIR}:/out:rw,z" \
        --entrypoint sh "$IMAGE" -c \
        'tar czf "/out/images_${TS}.tar.gz" -C /app/data images midjourney 2>/dev/null || true'
    echo "    $(du -h "${BACKUP_DIR}/images_${ts}.tar.gz" 2>/dev/null | cut -f1 || echo '?')  ${BACKUP_DIR}/images_${ts}.tar.gz"
    find "$BACKUP_DIR" -maxdepth 1 -name 'images_*.tar.gz' -mtime "+${SINNER_IMAGE_RETENTION_DAYS:-30}" -print -delete || true
fi

if [ -n "$RCLONE_REMOTE" ]; then
    echo "==> syncing ${BACKUP_DIR} -> ${RCLONE_REMOTE}"
    rclone copy "$BACKUP_DIR" "$RCLONE_REMOTE" --include 'db_*.sqlite3.gz' --include 'images_*.tar.gz'
fi

echo "==> done"
