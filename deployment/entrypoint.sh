#!/usr/bin/env bash
set -euo pipefail

# WORKDIR is /app, but the script now lives at /entrypoint.sh — be explicit.
cd /app

mkdir -p data/images/npc_creator/npcs data/midjourney data/media

if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
    python manage.py createsuperuser --no-input || true
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# bind / workers / logging live in gunicorn.conf.py
gunicorn shadowrun.wsgi --daemon

exec nginx -g 'daemon off;'
