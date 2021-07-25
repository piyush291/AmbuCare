from django.apps import AppConfig


class PatConfig(AppConfig):
    name = 'pat'

    def ready(self):
        import pat.signals
