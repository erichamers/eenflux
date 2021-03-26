from typing import List
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .forms import CreateCampaignForm
from .models import Campaign


class IndexView(ListView):
    template_name = 'website/index.html'
    model = Campaign
    context_object_name = 'campaigns'

class CreateCampaignView(CreateView):
    template_name = 'website/create_campaign.html'
    form_class = CreateCampaignForm
    
    def get_success_url(self) -> str:
        return reverse('website:index')

    def form_valid(self, form):
        form.instance.business = self.request.user.business
        return super().form_valid(form)