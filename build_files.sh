#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# install and build tailwindcss
npm install
python manage.py tailwind install
python manage.py tailwind build

# create superuser using creat-superuser.py file
python create-superuser.py






