#!/bin/sh

# Run the application
# Shell will fail if executation fails

set -e

echo "✅ Postgres is available ♫♪ - Starting the Application ⏩"

sleep 5

python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000

exec $@