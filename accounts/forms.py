from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone_number', 'profile_pic']
