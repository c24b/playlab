from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.db import models
from jsonfield import JSONField
import re
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from allauth.account.models import EmailAddress



#from model_utils.managers import InheritanceQuerySet
# Create your models here.

from fontawesome.fields import IconField

class Category(models.Model):
    icon = IconField()

class CustomUser(AbstractUser):
    genders = (('male','M'),('female','F'))
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(choices=genders, 
                               default="F", 
                               max_length=20, blank=True)
    # to enforce that you require email field to be associated with
    # every user at registration
    REQUIRED_FIELDS = ["email"]

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser)
    
    
class Team(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(CustomUser)
    date = models.DateTimeField(auto_now_add=True)

class Script(models.Model):
    ''' script form and model should be created throught a params.yaml '''
    TYPES = (
        ('C', 'Corpus'),
        ('A', 'Analysis'),
        )
    CAT = (
        (0, "build"),
        (1, "enrich"),
        (2, "textual"),
        (3, "explore"),
        (4, "analyse")
        )
    #LIST = find by listing scripts inside dir
    LEVEL =(
        ('S', 'User'),
        ('M', 'Dev'),
        ('L', 'Admin'),
        )
    level = models.CharField(('type'), max_length=1, choices=LEVEL)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)
    script_type = models.CharField(('type'), max_length=1, choices=TYPES)
    cat = models.CharField(('type'), max_length=1, choices=CAT)
    params = JSONField()

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    script = models.OneToOneField(Script, verbose_name="script")
    nb = models.IntegerField()
    params = JSONField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser)
    status = models.BooleanField()
    
def create_user_CustomUser(sender, instance, created, **kwargs):
    if created:
       CustomUser, created = CustomUser.objects.get_or_create(user=instance)

def create_project(**kwargs):
    pass
def create_job(**kwargs):
    pass

def create_script(**kwargs):
    pass
    #CustomUser, created = CustomUser.objects.get_or_create(user=instance)
