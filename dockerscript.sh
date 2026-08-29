#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

TAG=$(git rev-parse --short HEAD 2>/dev/null || date +%Y%m%d-%H%M)

# 1. Build the frontend on the host.
#    (Kept here on purpose: src/config.js is not env-aware yet and there is no
#    package-lock.json, so this is not safe to move into Docker as-is.)
( cd frontend && npm install && npm run build )

# 2. (add a DB backup step here if you want one)

# 3. Build the image and keep a tagged copy for rollback.
docker compose build
docker tag sinner:latest "sinner:${TAG}"
echo "built sinner:${TAG}"

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
