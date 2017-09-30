from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import rds


@receiver(user_logged_in)
def on_user_login(sender, **kwargs):
    rds.sadd('userlist', kwargs.get('user'))


@receiver(user_logged_out)
def on_user_logout(sender, **kwargs):
    rds.srem('userlist', kwargs.get('user'))
