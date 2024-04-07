#!/bin/bash

set -e

# Wait for database running:
sleep 5

if [[ ! -z $DATABASE_URL ]]; then
	while [[ $(nc -z $db_host 5432 &> /dev/null; echo $?) -ne 0 ]]; do echo pod is not running;sleep 3; done
fi

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn mce.wsgi:application --bind :8000
