from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import UpdateView

from .models import Campaign


class CampaignDetailsView(LoginRequiredMixin, UpdateView):
    template_name = 'campaigns/campaign_details.html'
    fields = ('ongoing',)   
    model = Campaign
    
    def get_success_url(self):
        return reverse('website:index')        


