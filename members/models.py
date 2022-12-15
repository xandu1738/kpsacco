from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Sacco(models.Model):
    name = models.CharField(max_length=255)
    sacco_id = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class RegisterMember(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=13)
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sacco_id = models.ForeignKey(Sacco, on_delete=models.SET_NULL, null=True)
    received = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
        
