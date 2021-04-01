from django.urls import path

from .views import CampaignDetailsView, CampaignsListView

app_name = 'campaigns'
urlpatterns = [
    path('campaigndetails/<int:pk>', CampaignDetailsView.as_view(), name='campaign-details'),
    path('campaigns/', CampaignsListView.as_view(), name='campaigns'),
]