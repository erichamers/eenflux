from django.urls import path

from .views import MyCampaignsView, CreateCampaignView, DeleteCampaignView

app_name = 'businesses'
urlpatterns = [
    path('mycampaigns', MyCampaignsView.as_view(), name='mycampaigns'),
    path('createcampaign', CreateCampaignView.as_view(), name='create-campaign'),
    path('delete/<int:pk>', DeleteCampaignView.as_view(), name='delete'),
]