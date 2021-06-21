from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Docs


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DocForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = ('title', 'document_up')

