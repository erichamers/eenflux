from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from .models import Campaign
from .forms import ApplicationForm


class CampaignDetailsView(LoginRequiredMixin, UpdateView):
    template_name = 'campaigns/campaign_details.html'
    fields = ('ongoing',)   
    model = Campaign
    
    def get_success_url(self):
        return reverse('website:index')        

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
