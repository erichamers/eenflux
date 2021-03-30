from django.shortcuts import render
from django.views.generic import TemplateView


class MyCamgaignsView(TemplateView):
    template_name = 'influencers/mycampaigns.html'