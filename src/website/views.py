from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView

from .forms import CreateCampaignForm, ApplicationForm
from .models import Campaign


class IndexView(LoginView):
    
    template_name = 'accounts/login.html'

class CreateCampaignView(LoginRequiredMixin, CreateView):
    
    template_name = 'website/business/create_campaign.html'
    form_class = CreateCampaignForm
    
    def form_valid(self, form):
        form.instance.business = self.request.user.business
        return super().form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        return reverse('website:mycampaigns')
    

class ApplicationView(LoginRequiredMixin, CreateView):
    
    template_name = 'website/details.html'
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
    

class MyCampaignsView(ListView):
    
    template_name = 'website/business/mycampaigns.html'
    model = Campaign
    context_object_name = 'campaigns'
    
    def get_queryset(self):
        return self.model.objects.filter(business_id=self.request.user.business.id)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        total_active = self.model.objects.filter(business_id=self.request.user.business.id, ongoing=True).count()
        total_finished = self.model.objects.filter(business_id=self.request.user.business.id, ongoing=False).count()
        context['active_count'] = total_active
        context['finished_count'] = total_finished
        return context
    

class DeleteCampaignView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('website:mycampaigns')
    template_name = 'website/business/campaign_confirm_delete.html'


class CampaignDetailsView(DetailView):
    template_name = 'website/campaign_details.html'
    queryset = Campaign.objects.all()