from django.apps import AppConfig


class VrConfig(AppConfig):
    name = 'vr'

    def ready(self):
        import vr.signals