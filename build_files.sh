#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# install and build tailwindcss
python manage.py tailwind build

# create superuser using creat-superuser.py file
python manage.py create-superuser.py






