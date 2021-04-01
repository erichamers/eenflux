from django.urls import path

from .views import CampaignDetailsView

app_name = 'campaigns'
urlpatterns = [
    path('campaigndetails/<int:pk>', CampaignDetailsView.as_view(), name='campaign-details'),
]