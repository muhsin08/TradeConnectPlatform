from .models import LoginDetails
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = LoginDetails
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = LoginDetails
        exclude = []