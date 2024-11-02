# your_app/management/commands/create_superuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dotenv import load_dotenv  # type: ignore
import os


class Command(BaseCommand):
    help = 'Create a superuser with a password'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                os.environ.get("SUPER_USER_USERNAME"),
                os.environ.get(
                    "SUPER_USER_EMAIL"),
                os.environ.get("SUPER_USER_PASSWORD")
            )
            self.stdout.write(self.style.SUCCESS(
                'Superuser created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
