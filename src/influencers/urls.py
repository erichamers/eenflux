from django.urls import path

from .views import MyCamgaignsView

app_name = 'influencers'
urlpatterns = [
    path('mycampaigns/', MyCamgaignsView.as_view(), name='my-campaigns')
]