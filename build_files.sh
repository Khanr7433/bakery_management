#!/bin/bash

# Install dependencies
pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

# Apply database migrations
python manage.py makemigrations || { echo "Failed to make migrations"; exit 1; }
python manage.py migrate || { echo "Failed to apply migrations"; exit 1; }

# Collect static files
python manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }

# Install and build tailwindcss
python manage.py tailwind build || { echo "Failed to build tailwindcss"; exit 1; }

# Create superuser using create-superuser command
python manage.py create-superuser || { echo "Failed to create superuser"; exit 1; }






