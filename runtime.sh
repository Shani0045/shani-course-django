#!/usr/bin/bash

python3 manage.py collectstatic --no-input
gunicorn shanicourse.wsgi:application --bind 0.0.0.0:8000
