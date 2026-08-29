#!/usr/bin/env bash
# Deploy: build frontend + image, back up the live DB, recreate the container.
#   SKIP_BACKUP=1 ./dockerscript.sh   skip the pre-deploy backup
set -euo pipefail
cd "$(dirname "$0")"

TAG=$(git rev-parse --short HEAD 2>/dev/null || date +%Y%m%d-%H%M)
CONTAINER="${SINNER_CONTAINER:-sinner}"

# 1. Build the frontend on the host.
#    (Kept here on purpose: src/config.js is not env-aware yet and there is no
#    package-lock.json, so this is not safe to move into Docker as-is.)
( cd frontend && npm install && npm run build )
# Generated NPC/location images are served by nginx from the data volume, not
# from the React build — drop them so they don't bloat the image.
rm -rf frontend/build/images/npc_creator frontend/build/images/npcs

# 2. Build the image and keep a tagged copy for rollback.
docker compose build
docker tag sinner:latest "sinner:${TAG}"
echo "built sinner:${TAG}"

# 3. Back up the live database before replacing the container.
#    Fatal on failure: don't discard a running DB we couldn't snapshot.
if [ "${SKIP_BACKUP:-0}" = "1" ]; then
    echo "==> skipping pre-deploy backup (SKIP_BACKUP=1)"
elif docker ps --format '{{.Names}}' | grep -qx "$CONTAINER"; then
    echo "==> pre-deploy backup"
    ./deployment/backup.sh
else
    echo "==> no running '$CONTAINER' container — nothing to back up yet"
fi

# 4. Recreate the container.
docker compose up -d

# 5. Wait for the healthcheck before calling it done.
printf 'waiting for health'
for i in $(seq 1 20); do
    status=$(docker inspect -f '{{.State.Health.Status}}' sinner 2>/dev/null || echo starting)
    if [ "$status" = "healthy" ]; then
        echo " OK (sinner:${TAG})"
        break
    fi
    if [ "$i" -eq 20 ]; then
        echo " FAILED"
        docker compose logs --tail=50 web
        echo "rollback:  docker tag sinner:<previous-tag> sinner:latest && docker compose up -d"
        exit 1
    fi
    printf '.'
    sleep 3
done

# 6. Drop dangling images.
docker image prune -f
