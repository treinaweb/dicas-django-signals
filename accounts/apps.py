from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.contrib.auth.models import User
        from django.db.models.signals import post_save

        from .signals import send_welcome_email

        post_save.connect(receiver=send_welcome_email, sender=User)