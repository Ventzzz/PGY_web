from django import forms
from django.forms import ModelForm
from .models import Bebidas
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BebidasForm(ModelForm):
    class Meta:
        model = Bebidas
        fields = "__all__"

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')