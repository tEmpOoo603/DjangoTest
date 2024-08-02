from django.contrib.auth.forms import AuthenticationForm

from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True,
                                                             "type": "text",
                                                             "class": "form-control",
                                                             "placeholder": "Введите ваше имя пользователя",
                                                             "required": True
                                                             }
                                                      ),
                               label="Имя пользователя"
                               )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                 "type": "password",
                                                                 "class": "form-control",
                                                                 "placeholder": "Введите ваш пароль",
                                                                 "required": True
                                                                 }
                                                          ),
                               label="Пароль"
                               )

    class Meta:
        model = User