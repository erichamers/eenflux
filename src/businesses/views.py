from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView

from campaigns.forms import CampaignForm
from campaigns.models import Campaign, Application


class CreateCampaignView(LoginRequiredMixin, CreateView):
    
    template_name = 'businesses/create_campaign.html'
    form_class = CampaignForm
    
    def form_valid(self, form):
        form.instance.business = self.request.user.business
        return super().form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        return reverse('businesses:mycampaigns')    


class MyCampaignsView(ListView):
    
    template_name = 'businesses/mycampaigns.html'
    model = Campaign
    context_object_name = 'campaigns'
    
    def get_queryset(self):
        return self.model.objects.filter(business_id=self.request.user.business.id, deleted=False)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        business_id = self.request.user.business.id
        campaigns = self.model.objects.filter(business_id=business_id)
        total_active = campaigns.filter(ongoing=True).count()
        total_finished = campaigns.filter(ongoing=False).count()
        total_applications = Application.objects.filter(campaign__business_id=business_id, rejected=False, accepted=False).count()
        
        campaigns_data = dict()
        for campaign in campaigns:
            campaigns_data[campaign.title] = Application.objects.filter(campaign__id=campaign.id).count()
        
        context['campaigns_data'] = campaigns_data
        context['active_count'] = total_active
        context['finished_count'] = total_finished
        context['total_applications'] = total_applications
        print(context)
        return context
    

class DeleteCampaignView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('businesses:mycampaigns')
    template_name = 'businesses/campaign_confirm_delete.html'
