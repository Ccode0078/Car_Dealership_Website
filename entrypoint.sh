#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset

: "${PORT:=8000}"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn dealership.wsgi:application \
  --bind 0.0.0.0:${PORT} \
  --workers ${WEB_CONCURRENCY:-3} \
  --timeout 120 \
  --log-level info \
  --access-logfile - \
  --error-logfile -

