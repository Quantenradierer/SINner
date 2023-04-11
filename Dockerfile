FROM python:3.11

RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y gunicorn

# configuring nginx
COPY ./deployment/nginx/default.conf /etc/nginx/sites-enabled/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

ENV PUBLIC_NPC_IMAGE_PATH='/app/data/images/npc_creator/npcs'

WORKDIR /app

COPY backend/ ./
RUN pip install -r ./requirements.txt

COPY deployment/entrypoint.sh ./entrypoint.sh
COPY frontend/build/ /www/data/

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
