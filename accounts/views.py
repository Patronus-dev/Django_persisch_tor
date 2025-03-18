from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from .forms import UserProfileEditForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class UserProfileView(DetailView):
    model = CustomUser
    template_name = "accounts/user_profile.html"
    context_object_name = "user_profile"

    def get_object(self):
        return self.request.user


class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileEditForm
    template_name = "accounts/user_profile_edit.html"
    success_url = reverse_lazy("user_profile")

    def get_object(self):
        return self.request.user
