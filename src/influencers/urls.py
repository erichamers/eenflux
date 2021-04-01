from django.urls import path

from .views import MyCamgaignsView, ApplicationView

app_name = 'influencers'
urlpatterns = [
    path('my-proposals/', MyCamgaignsView.as_view(), name='my-proposals'),
    path('apply/<int:pk>', ApplicationView.as_view(), name='apply'),
]