from django.urls import path

from .views import CampaignDetailsView, ApplicationView

app_name = 'campaigns'
urlpatterns = [
    path('campaigndetails/<int:pk>', CampaignDetailsView.as_view(), name='campaign-details'),
    path('apply/<int:pk>', ApplicationView.as_view(), name='apply'),
]