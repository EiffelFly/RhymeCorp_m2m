from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry

'''
    We want to store extra information in existing User model 
    which is not related to authentication process so we use
    OnetoOneField to connect to user model.
    further information: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_stellar_keyword_sum = models.IntegerField(
        verbose_name=_('Stellar Keyword Sum'),
        default=0,
        blank=True
    )
    user_basestone_keyword_sum = models.IntegerField(
        verbose_name=_('Stellar Keyword Sum'),
        default=0,
        blank=True
    )

'''
    In order to use this kind of method, we are going to define
    "signal" to make model-Profile created/updated when model-User
    created/updated.
'''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if not getattr(instance, "profile", None):
            Profile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()