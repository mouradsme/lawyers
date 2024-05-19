#!usr/bin/env bash

echo "Buidling project packages..."
python3 -m pip install -r requirements.txt

echo "Run Migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput