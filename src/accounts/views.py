from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
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

    def get_success_url(self):
        if self.request.user.user_type == 'BZ':
            return reverse('businesses:mycampaigns')
        else:
            return reverse('influencers:my-campaigns')
    
    def get(self, request, *args, **kwargs):
        """
        Redirects to index page is user is already logged in
        """
        if request.user.is_authenticated:
            if request.user.user_type == 'BZ':
                return redirect('/businesses/mycampaigns')
            if request.user.user_type == 'IN':
                return redirect('/influencers/mycampaigns')
        return super().get(request)