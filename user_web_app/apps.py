from django.apps import AppConfig


class UserWebAppConfig(AppConfig):
    name = 'user_web_app'
    def ready(self):
        import user_web_app.signals
