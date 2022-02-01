from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import member
from django import forms


class memberRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = member
        fields = ['profile_pic']