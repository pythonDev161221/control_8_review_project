from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms


class MyUserCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")


User = get_user_model()


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        # labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}

