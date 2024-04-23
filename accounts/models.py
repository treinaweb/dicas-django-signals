from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail


# @receiver(post_save, sender=User)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created and instance.email:
#         send_mail(
#             "Boas Vindas",
#             "Seja bem vindo ao nosso site",
#             "no-reply@treinaweb.com.br",
#             [instance.email],
#         )


# @receiver(pre_save, sender=User)
# def pre_save_func(sender, **kwargs):
#     print("********** Pre Save **********")
#     print(sender)
#     print(kwargs)
#     print("******************************")

# @receiver(post_save, sender=User)
# def post_save_func(sender, **kwargs):
#     print("********** Post Save **********")
#     print(sender)
#     print(kwargs)
#     print("*******************************")

# @receiver(pre_delete, sender=User)
# def pre_delete_func(sender, **kwargs):
#     print("********** Pre Delete **********")
#     print(sender)
#     print(kwargs)
#     print("********************************")

# @receiver(post_delete, sender=User)
# def post_delete_func(sender, **kwargs):
#     print("********** Post Delete **********")
#     print(sender)
#     print(kwargs)
#     print("*********************************")