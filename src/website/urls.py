from django.urls import path

from .views import IndexView, CreateCampaignView, ApplicationView

app_name = 'website'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('newcampaign/', CreateCampaignView.as_view(), name='new-campaign'),
    path('apply/<int:pk>', ApplicationView.as_view(), name='apply'),
]
