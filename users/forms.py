from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        # fields = '__all__'
        exclude = ('user',) # Burada virgülü unutma



