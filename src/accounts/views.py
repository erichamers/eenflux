from django.shortcuts import redirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import CreateUserForm


class RegisterView(CreateView):
    
    template_name = 'accounts/register.html'
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('website:index')
    
    def get(self, request, *args, **kwargs):
        """
        Redirects to index page is user is already logged in
        """
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request)
    
    def form_valid(self, form):
        return super().form_valid(form)
            
        

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self) -> str:
        if self.request.user.user_type == 'BZ':
            return reverse('website:mycampaigns', kwargs={'pk': self.request.user.id})
        else:
            return reverse('website:mycampaigns', kwargs={'pk': self.request.user.id})
    
    def get(self, request, *args, **kwargs):
        """
        Redirects to index page is user is already logged in
        """
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request)