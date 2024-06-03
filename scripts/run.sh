#!/bin/bash

# Run the application
# Shell will fail if executation fails

python3 manage.py collectstatic --noinput
python3 manage.py migrate
# python3 manage.py createsuperuser --noinput --email ${DJANGO_SUPERUSER_EMAIL}
python3 manage.py runserver localhost:8000
