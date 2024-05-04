from time import sleep

from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    # def ready(self):
    #     from main.scheduler import start_scheduler
    #     sleep(3)
    #     start_scheduler()

