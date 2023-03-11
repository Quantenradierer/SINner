FROM python:3.11

RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y gunicorn


# configuring nginx
COPY ./deployment/nginx/default.conf /etc/nginx/sites-enabled/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log


ARG OPENAI_API_KEY
ARG MJ_CHANNEL_ID
ARG MJ_PRIVATE_DISCORD_TOKEN
ARG MJ_SERVER_ID

ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV MJ_CHANNEL_ID=$MJ_CHANNEL_ID
ENV MJ_PRIVATE_DISCORD_TOKEN=$MJ_PRIVATE_DISCORD_TOKEN
ENV MJ_SERVER_ID=$MJ_SERVER_ID
ENV PUBLIC_NPC_IMAGE_PATH='/www/data/images/npcs/'

WORKDIR /app

COPY backend/ ./
RUN pip install -r ./requirements.txt
RUN pip install gunicorn
RUN pip install gevent
ENV FLASK_ENV production

RUN mkdir ./data
RUN mkdir ./data/midjourney

COPY data/npcs.sqlite ./data/
COPY data/midjourney_banned_words.txt ./data/
COPY frontend/build/ /www/data/
COPY deployment/config ./config


RUN chmod +x config/entrypoint.sh

CMD ["./config/entrypoint.sh"]