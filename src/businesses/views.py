from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView

from campaigns.forms import CampaignForm
from campaigns.models import Campaign


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
        total_active = self.model.objects.filter(business_id=self.request.user.business.id, ongoing=True).count()
        total_finished = self.model.objects.filter(business_id=self.request.user.business.id, ongoing=False).count()
        context['active_count'] = total_active
        context['finished_count'] = total_finished
        return context
    

class DeleteCampaignView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('businesses:mycampaigns')
    template_name = 'businesses/campaign_confirm_delete.html'
