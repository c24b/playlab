from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.db import models
from jsonfield import JSONField
import re
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress



#from model_utils.managers import InheritanceQuerySet
# Create your models here.

from fontawesome.fields import IconField

class Category(models.Model):
    icon = IconField()
    
class Profile(models.Model):
    ''' Unique User extended auth throught one of these methods'''
    ROLES = (
        ('S', 'User'),
        ('M', 'Dev'),
        ('L', 'Admin'),)
    role = models.CharField(max_length=1, choices=ROLES, default='S')
    user = models.OneToOneField(User, related_name='user')
    
    # user visible settings
    stop_reminders = models.BooleanField ( default=False,
                             help_text = 'Flag if user wants reminders not to be sent.' )

    stop_all_email = models.BooleanField ( default=False,
                             help_text = 'Flag if user wants no email to be sent.' )

    # hidden settings
    is_premium =  models.BooleanField ( default=False,
                             help_text = 'Flag if user has the premium service.' )
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        if self.user.email:
            return "{}'s profile".format(self.user.email)
        else:
            return "{}'s profile".format(self.user.username)
    
    #social_account
    #email = models.EmailField(max_length=30,blank=True)
    
    #~ username = models.CharField(max_length=40)
    def get_username(self):
        if self.user.username is not None:
            return self.username
        else:
           if self.user.email is not None:
               self.user.username = re.split("@", self.user.email)[0]
 
    
    def change_role(self, role):
        print role
        #self.role = models.CharField(max_length=1, choices=ROLES, default='S')
        #self.save()
        
    def social_account_exists(self):
        pass
    
    #~ def account_verified(self):
        #~ if self.user.is_authenticated:
            #~ result = EmailAddress.objects.filter(email=self.email)
            #~ if len(result):
                #~ return result[0].verified
        #~ return False

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile)
    
    
class Team(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Profile)
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
    user = models.ForeignKey(Profile)
    status = models.BooleanField()
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Profile.objects.get_or_create(user=instance)

def create_project(**kwargs):
    pass
def create_job(**kwargs):
    pass

def create_script(**kwargs):
    pass
    #profile, created = Profile.objects.get_or_create(user=instance)
