from django.urls import path

from .views import IndexView, CreateCampaignView

app_name = 'website'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('newcampaign/', CreateCampaignView.as_view(), name='new-campaign'),
]
