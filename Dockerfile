FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PUBLIC_IMAGE_PATH='/app/data/images/npc_creator/'

# nginx only. gunicorn comes from requirements.txt, not apt.
# If a Python dependency ever needs to compile, add build-essential here.
RUN apt-get update \
    && apt-get install -y --no-install-recommends nginx \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

COPY ./deployment/nginx/default.conf /etc/nginx/sites-enabled/default

WORKDIR /app

# Dependencies first so code changes don't reinstall the world.
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt

COPY backend/ ./
COPY deployment/entrypoint.sh ./entrypoint.sh
COPY frontend/build/ /www/data/

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
