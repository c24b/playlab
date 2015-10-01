from django import forms
#from .models import *

class UserProfileForm(forms.Form):
    def __init__(self,req="request",instance={}):
        self.req = req
        self.instance = instance
    
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='First name', max_length=30)
    username = forms.CharField(label='First name', max_length=30)
    email = forms.EmailField(label='First name', max_length=30)
    

