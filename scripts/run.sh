#!/bin/bash

# Run the application
# Shell will fail if executation fails

/venv/bin/python3 /gamma_budget/manage.py collectstatic --noinput
/venv/bin/python3 /gamma_budget/manage.py migrate
# /venv/bin/python3 /gamma_budget/manage.py createsuperuser --noinput --email ${DJANGO_SUPERUSER_EMAIL}
/venv/bin/python3 /gamma_budget/manage.py runserver 0.0.0.0:8000
