# Schattenakte Readme
![Animation.gif](docs%2FAnimation.gif)

This project is still work in progress. If you see something strange or something isn't working just write me! I am always eager to help, even for small things.

Schattenakte is an application to create NPCs for Shadowrun Pen&Paper.
It uses GPT for NPCs description, and midjourney to create images.
The image generation is a bit of manual labor currently, since there is no actual API. 

The backend is Python based (Django), while the frontend uses React and Arwes (https://arwes.dev/).

# Installation

## Environment Variables

Invite a midjourney bot to your server: https://docs.midjourney.com/docs/invite-the-bot
I recommend setting up a private channel to not disturb anyone.

Copy the `.env.example` to `.env`: `cp .env.example .env`.

Please set the env variables in the `.env` file:

| ENV Variable             | Description                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------|
| OPENAI_API_KEY           | Create and copy the api key from: https://platform.openai.com/account/api-keys                   |
| MJ_SERVER_ID             | Your Discord server ID (right click on server -> Copy ID)                                        |
| MJ_CHANNEL_ID            | Your Discord channel ID (right click on channel -> Copy ID)                                      |
| MJ_PRIVATE_DISCORD_TOKEN | see https://linuxhint.com/get-discord-token/ how to get it                                       |
| DJANGO_SECURE_KEY        | `from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())` |
| DJANGO_HOST              | localhost or your domain                                                                         |
| DJANGO_PORT              | like, 8000 or 80                                                                                 |



## Frontend
Download and Install NPM: https://www.npmjs.com/ 
```
cd frontend
npm install
```
Then you can run it with `npm start`. If there is no Backend running, it will result in an error page.
Look into frontend/README for further instructions.

## Backend
Download and Install Python: https://www.python.org/

(if you installed the frontend previously, don't forget to go back into the project root, with `cd ..`)
```
pip install -r backend\requirements.txt
cd backend
python manage.py migrate
python manage.py runserver
```

It will create one npc and then start the flask backend server.
However, at the moment the image won't be created. This is still WIP. 

# Costs

GPT-3.5 costs $0.002 / 1K tokens. One NPC call is around 1.3K tokens.
Even with planned changes and additional features, it will be around 0.01$ per npc creation.

Midjourney costs 8$ for ca. 200 generations in the cheapest subscription plan.
This means 0.04$ per NPC, but you can choose between 4 images.

In summary, it costs around 0.05$ per NPC creation. 

I would like to add other AI image generators, so if you have experience with other AI image generators, please let me know.
I have tried DALL-E 2, but the results are not suitable.

# Docker

The app runs as a single container (nginx + gunicorn), managed with Docker Compose.

## First-time setup on the server

1. Create the data volume (database + images):
   `docker volume create sinner-data`
2. Create the environment file:
   `cp deployment/env.example .env` and fill it in.
   `.env` lives in the repo root, is git-ignored, and is injected by Compose —
   it is never baked into the image.

## Deploying

Run `./dockerscript.sh`. It builds the frontend on the host, builds the image,
tags it with the current commit (`sinner:<sha>`) for rollback, recreates the
container via `docker compose up -d`, and waits for the healthcheck.

Other useful commands:

- `docker compose logs -f web` — follow logs
- `docker compose ps` — status (shows `healthy` / `unhealthy`)
- Rollback: `docker tag sinner:<previous-sha> sinner:latest && docker compose up -d`

## Backups

`deployment/backup.sh` and `deployment/restore.sh` handle consistent SQLite
snapshots, retention and offsite copies. See `deployment/BACKUP.md`.
