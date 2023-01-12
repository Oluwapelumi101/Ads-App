#!/bin/sh

APP_PORT=${PORT:-8000}
# cd /mysite/


/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm mysite.wsgi:application --bind "0.0.0.0:${APP_PORT}"

exec "$@" 