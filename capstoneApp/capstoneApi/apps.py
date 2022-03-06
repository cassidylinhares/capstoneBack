from django.apps import AppConfig


class CapstoneapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'capstoneApi'

    def ready(self) -> None:
        from scheduler.scheduler import start
        start()
