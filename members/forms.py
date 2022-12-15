from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class SaccoForm(ModelForm):
    class Meta:
        model = Sacco
        fields = ['name']
        
class MemberRegForm(ModelForm):
    class Meta:
        model = RegisterMember
        fields = ['name','tel', 'inviter', 'sacco_id']