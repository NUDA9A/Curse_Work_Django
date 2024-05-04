from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Download fixtures to files from all apps"

    def handle(self, *args, **options):
        call_command("dumpdata", "auth", "-o", "data/auth_data.json")
        call_command("dumpdata", "users", "-o", "data/users_data.json")
        call_command("dumpdata", "blogs", "-o", "data/blog_data.json")
        call_command("dumpdata", "main", "-o", "data/main_data.json")
