from django.contrib.auth.forms import UserCreationForm

from webapp import forms


class MyUserCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")


