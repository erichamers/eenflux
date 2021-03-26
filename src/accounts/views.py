from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import UserCreationForm


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('website:index')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self) -> str:
        return reverse('website:index')