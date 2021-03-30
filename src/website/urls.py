from django.urls import path

from .views import (IndexView, CreateCampaignView, ApplicationView, 
                    MyCampaignsView, DeleteCampaignView, CampaignDetailsView)

app_name = 'website'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('createcampaign/', CreateCampaignView.as_view(), name='create-campaign'),
    path('apply/<int:pk>', ApplicationView.as_view(), name='apply'),
    path('mycampaigns/', MyCampaignsView.as_view(), name='mycampaigns'),
    path('delete/<int:pk>', DeleteCampaignView.as_view(), name='delete'),
    path('campaigndetails/<int:pk>', CampaignDetailsView.as_view(), name='campaign-details')
]
