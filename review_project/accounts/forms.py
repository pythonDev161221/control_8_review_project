from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms


class MyUserCreateForm(UserCreationForm):

    email = forms.EmailField(
        label="email", required=True
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def clean(self):
        cleaned_data = super(MyUserCreateForm, self).clean()
        if not cleaned_data['email']:
            raise ValueError('email is required')
        return cleaned_data


User = get_user_model()


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
