from typing import List
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import CreateCampaignForm, ApplicationForm
from .models import Campaign, Application


class IndexView(ListView):
    
    template_name = 'website/index.html'
    model = Campaign
    context_object_name = 'campaigns'

class CreateCampaignView(CreateView):
    
    template_name = 'website/business/create_campaign.html'
    form_class = CreateCampaignForm
    
    def form_valid(self, form):
        form.instance.business = self.request.user.business
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('website:index')
    

class ApplicationView(CreateView):
    
    template_name = 'website/apply.html'
    form_class = ApplicationForm
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign = Campaign.objects.get(pk=self.kwargs.get('pk'))
        context['campaign'] = campaign
        return context
    
    def form_valid(self, form):
        form.instance.campaign_id = self.get_context_data()['campaign'].id
        form.instance.influencer_id = self.request.user.influencer.id
        return super().form_valid(form)  
          
    def get_success_url(self):
        return reverse('website:index')
