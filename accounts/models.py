from __future__ import unicode_literals

from django.contrib import auth
from django.db import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)


# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class User_detail(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=264, unique=True)

    def __unicode__(self):
        return self.firstname


# codes for user registration.
class UserProfileInfo(models.Model):
    INTEREST_CHOICES = (
        ('Individual Sports (Marathon Running) ', 'Individual Sports (Marathon Running) '),
        ('Team Sports (Basketball) ', 'Team Sports (Basketball) '),
        ('Extreme Sports (Motocross) ', 'Extreme Sports (Motocross) '),
        ('Tech Hobbies (Computing)', 'Tech Hobbies (Computing)'),
        ('Puzzles (Crosswords)', 'Puzzles (Crosswords)'),
        ('Games (Chess)', 'Games (Chess)'),
        ('Games (Chess)', 'Games (Chess)'),
    )
    interest = models.CharField(max_length=6, choices=INTEREST_CHOICES, default='green')
    # one to one relation between defined user mode
    user = models.OneToOneField(User)
    portfolio_site = models.URLField(blank=True)
    city = models.CharField(max_length=20,default="KOLKATA")
    state = models.CharField(max_length=20,default="West-Bengal")

    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __unicode__(self):
        return self.user.name
