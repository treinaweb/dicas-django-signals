from django.core.mail import send_mail

def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:
        send_mail(
            "Boas Vindas",
            "Seja bem vindo ao nosso site",
            "no-reply@treinaweb.com.br",
            [instance.email],
        )