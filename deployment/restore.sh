#!/usr/bin/env bash
# Restore the sinner SQLite database from a backup made by backup.sh.
#
#   deployment/restore.sh latest              # newest backup in SINNER_BACKUP_DIR
#   deployment/restore.sh /path/db_....gz     # a specific file (.gz or plain)
#   deployment/restore.sh --yes latest        # skip the confirmation prompt
#
# It stops the app, snapshots the current DB to  pre-restore_<ts>.sqlite3  next
# to the source file, swaps in the backup, integrity-checks it (rolling back on
# failure), then starts the app and waits for the healthcheck.
#
# Config via environment (all optional):
#   SINNER_CONTAINER   container name     (default: sinner)
#   SINNER_BACKUP_DIR  backup location    (default: /srv/backups/sinner)
#   SINNER_IMAGE       throwaway image    (default: sinner:latest)
#   SINNER_VOLUME      data volume name   (default: sinner-data)
set -euo pipefail

CONTAINER="${SINNER_CONTAINER:-sinner}"
BACKUP_DIR="${SINNER_BACKUP_DIR:-/srv/backups/sinner}"
IMAGE="${SINNER_IMAGE:-sinner:latest}"
VOLUME="${SINNER_VOLUME:-sinner-data}"
COMPOSE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ASSUME_YES=0

compose() { ( cd "$COMPOSE_DIR" && docker compose "$@" ); }
usage() { echo "usage: $0 [--yes] <backup-file|latest>" >&2; exit 1; }

[ $# -ge 1 ] || usage
SRC=""
while [ $# -gt 0 ]; do
    case "$1" in
        --yes|-y) ASSUME_YES=1 ;;
        -h|--help) usage ;;
        *) SRC="$1" ;;
    esac
    shift
done
[ -n "$SRC" ] || usage

command -v docker >/dev/null || { echo "error: docker not found" >&2; exit 1; }

if [ "$SRC" = "latest" ]; then
    SRC="$(ls -1t "${BACKUP_DIR}"/db_*.sqlite3.gz "${BACKUP_DIR}"/db_*.sqlite3 2>/dev/null | head -n1 || true)"
    [ -n "$SRC" ] || { echo "error: no db_* backups in ${BACKUP_DIR}" >&2; exit 1; }
fi
[ -f "$SRC" ] || { echo "error: not a file: $SRC" >&2; exit 1; }
SRC="$(cd "$(dirname "$SRC")" && pwd)/$(basename "$SRC")"
SRC_DIR="$(dirname "$SRC")"
SRC_NAME="$(basename "$SRC")"
ts="$(date +%Y-%m-%d_%H%M%S)"

echo "restore source : $SRC"
echo "target         : volume ${VOLUME} (container ${CONTAINER})"
echo "safety copy    : ${SRC_DIR}/pre-restore_${ts}.sqlite3"
if [ "$ASSUME_YES" -ne 1 ]; then
    printf "This overwrites the LIVE database. Type 'restore' to continue: "
    read -r ans
    [ "$ans" = "restore" ] || { echo "aborted"; exit 1; }
fi

echo "==> stopping app"
compose stop web

echo "==> snapshotting current DB and swapping in the backup"
if ! docker run --rm -i \
        -e SRC_NAME="$SRC_NAME" -e TS="$ts" \
        -v "${VOLUME}:/app/data" -v "${SRC_DIR}:/backups:rw" \
        --entrypoint sh "$IMAGE" -s <<'EOSH'
set -e
if [ -f /app/data/db.sqlite3 ]; then
    cp /app/data/db.sqlite3 "/backups/pre-restore_${TS}.sqlite3"
fi
case "$SRC_NAME" in
    *.gz) gunzip -c "/backups/${SRC_NAME}" > /app/data/db.sqlite3 ;;
    *)    cp "/backups/${SRC_NAME}" /app/data/db.sqlite3 ;;
esac
rm -f /app/data/db.sqlite3-wal /app/data/db.sqlite3-shm /app/data/db.sqlite3-journal
r=$(python -c "import sqlite3; print(sqlite3.connect('/app/data/db.sqlite3').execute('PRAGMA integrity_check').fetchone()[0])")
echo "    integrity_check: $r"
[ "$r" = ok ]
EOSH
then
    echo "!! integrity check failed — rolling back to pre-restore snapshot" >&2
    docker run --rm -i -e TS="$ts" \
        -v "${VOLUME}:/app/data" -v "${SRC_DIR}:/backups:rw" \
        --entrypoint sh "$IMAGE" -s <<'EOSH'
set -e
cp "/backups/pre-restore_${TS}.sqlite3" /app/data/db.sqlite3
rm -f /app/data/db.sqlite3-wal /app/data/db.sqlite3-shm /app/data/db.sqlite3-journal
EOSH
    compose up -d
    echo "rolled back. app restarted with the previous database." >&2
    exit 1
fi

echo "==> starting app"
compose up -d

echo -n "==> waiting for health"
for i in $(seq 1 20); do
    s="$(docker inspect -f '{{.State.Health.Status}}' "$CONTAINER" 2>/dev/null || echo starting)"
    if [ "$s" = "healthy" ]; then
        echo " OK"
        echo "restore complete. previous DB kept at ${SRC_DIR}/pre-restore_${ts}.sqlite3"
        exit 0
    fi
    [ "$i" -eq 20 ] && { echo " FAILED"; compose logs --tail=50 web; exit 1; }
    echo -n "."
    sleep 3
done
