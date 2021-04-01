from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .models import Campaign, Application


class CampaignDetailsView(LoginRequiredMixin, UpdateView):
    template_name = 'campaigns/campaign_details.html'
    fields = ('ongoing',)   
    model = Campaign
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applications'] = Application.objects.filter(campaign_id=context.get('campaign').id)
        return context
    
    def get_success_url(self):
        return reverse('website:index')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        applications = Application.objects.filter(campaign__id=self.object.id)
        for application in applications:
            if not application.accepted:
                application.rejected = True
                application.save()
        return super(CampaignDetailsView, self).post(request, *args, **kwargs)


class CampaignsListView(ListView):
    template_name = 'campaigns/list_campaigns.html'
    model = Campaign
    context_object_name = 'campaigns'

    def get_queryset(self):
        print(self.request.GET)
        query = self.request.GET.get('q', None)
        object_list = self.model.objects.all()
        if query:
            object_list = self.model.objects.filter(Q(title__contains=query))
        return object_list