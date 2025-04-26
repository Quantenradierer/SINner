#!/bin/bash

mkdir data/images
mkdir data/images/npc_creator/
mkdir data/images/npc_creator/npcs
mkdir data/midjourney

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn shadowrun.wsgi --bind 0.0.0.0:8010 --workers 6 --daemon

nginx -g 'daemon off;'