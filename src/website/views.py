from django import views
from django.shortcuts import redirect


class IndexView(views.View):
    
    def get(self, *args, **kwargs):
        return redirect('accounts/login')