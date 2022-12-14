#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@admin.com"}
cd /code/

/opt/venv/bin/python manage.py migrate --noinput

# # Collect static files
RUN /opt/venv/bin/python manage.py manage.py collectstatic --noinput

/opt/venv/bin/python manage.py createsuperuser --email=admin@admin.com  --noinput || true