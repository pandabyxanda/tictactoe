import random

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


# from django.contrib.auth.models import User
# from captcha.fields import CaptchaField

class PlayerNameForm(forms.Form):
    player_name = forms.CharField(
        widget=forms.Textarea(attrs={'id':"player_name"}),
        label=''
    )

