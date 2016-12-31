from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #account types
    is_client = models.BooleanField('is_client', default=True)
    is_washr = models.BooleanField('is_washr', default=False)
    is_superuser = models.BooleanField('is_superuser', default=False)

    #other fields here
    avatar = models.ImageField('avatar', upload_to='media', null=True, blank=True)
    phone = models.CharField('phone number', max_length=20, blank=True, default='')
    address = models.CharField('address', max_length=100, default='', blank=True)
    city = models.CharField('city', max_length=100, default='', blank=True)
    state = models.CharField('state', max_length=2, default='', blank=True)
    country = models.CharField('country', max_length=100, default='', blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
