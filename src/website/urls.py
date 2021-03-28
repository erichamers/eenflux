from django.urls import path

from .views import IndexView, CreateCampaignView, ApplicationView

app_name = 'website'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('createcampaign/', CreateCampaignView.as_view(), name='create-campaign'),
    path('apply/<int:pk>', ApplicationView.as_view(), name='apply'),
]
