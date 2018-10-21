from django.db import models
from builtins import *
from django.contrib.auth.models import User
from django import forms

# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField("Website", blank=True)
    bio = models.CharField(max_length=80, blank=True)
    birthdate = forms.DateTimeField(
        widget=forms.widgets.DateInput(format="%d/%m/%y"))