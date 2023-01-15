#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@admin.com"}

# Handling migrations
python manage.py migrate --noinput

# # Collect static files
python manage.py collectstatic --noinput

# creating admin
python manage.py createsuperuser --email=admin@admin.com  --noinput || true

ls