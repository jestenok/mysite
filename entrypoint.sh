#!/bin/sh
python manage.py makemigrations
python manage.py migrate

python manage.py createcachetable

python manage.py createsuperuser --noinput --username ${LOGIN} --email ${LOGIN}@${DOMAINNAME}

gunicorn mysite.wsgi:application --bind 0.0.0.0:8000

exec "$@"