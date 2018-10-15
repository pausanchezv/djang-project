# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
    """ User profile manager """

    def get_queryset(self):
        """ Queryset getter """
        return super(UserProfileManager, self).get_queryset().filter(city='Barna')


class UserProfile(models.Model):
    """ User Model """

    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    barna = UserProfileManager()
    objects = models.Manager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile, sender=User)