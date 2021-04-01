from django.urls import reverse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from campaigns.models import Application, Campaign
from campaigns.forms import ApplicationForm


class MyCamgaignsView(ListView):
    template_name = 'influencers/my-proposals.html'
    model = Application

    def get_context_data(self):
        context = super(MyCamgaignsView, self).get_context_data()
        total_accepted = self.model.objects.filter(influencer_id=self.request.user.influencer.id, accepted=True).count()
        total_rejected = self.model.objects.filter(influencer_id=self.request.user.influencer.id, rejected=True).count()
        total_opened = self.model.objects.filter(influencer_id=self.request.user.influencer.id, rejected=False, accepted=False).count()
        context['total_accepted'] = total_accepted
        context['total_rejected'] = total_rejected
        context['total_opened'] = total_opened
        context['applications'] = self.model.objects.filter(influencer_id=self.request.user.influencer.id)
        return context
    

class ApplicationView(LoginRequiredMixin, CreateView):
    
    template_name = 'influencers/apply.html'
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

class ApplicationDetailsView(DetailView):
    template_name = 'influencers/application_details.html'
    model = Application