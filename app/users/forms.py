from django.contrib.auth.forms import AuthenticationForm

from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    class Meta:
        models = User