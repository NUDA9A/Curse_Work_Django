from django.core.management.base import BaseCommand

from main.scheduler import start_scheduler


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_scheduler()
