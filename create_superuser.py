# your_app/management/commands/create_superuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import environ
env = environ.Env()


class Command(BaseCommand):
    help = 'Create a superuser with a password'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(env('SUPER_USER_USERNAME'), env(
                'SUPER_USER_EMAIL'), env('SUPER_USER_PASSWORD'))
            self.stdout.write(self.style.SUCCESS(
                'Superuser created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
