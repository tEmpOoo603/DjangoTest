from django.contrib.auth.forms import AuthenticationForm

from users.models import Users


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User