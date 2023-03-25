from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'id': 'username',
        'class': 'input'
    }))
    email = forms.EmailField(max_length=128, widget=forms.EmailInput(attrs={
        'id': 'email',
        'class': 'input'
    }))
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={
        'id': 'password',
        'class': 'input'
    }), validators=(password_validation.validate_password, ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UserEnterForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'id': 'username',
        'class': 'input'
    }))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={
        'id': 'password',
        'class': 'input'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'id': 'username',
        'class': 'input'
    }))
    email = forms.EmailField(max_length=128, widget=forms.EmailInput(attrs={
        'id': 'email',
        'class': 'input'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')