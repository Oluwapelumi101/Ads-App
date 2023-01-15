#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@admin.com"}
# cd /mysite/


# Handling migrations
/opt/venv/bin/python manage.py migrate --noinput

# # Collect static files
/opt/venv/bin/python manage.py collectstatic --noinput

# creating admin
/opt/venv/bin/python manage.py createsuperuser --email=admin@admin.com  --noinput || true

ls