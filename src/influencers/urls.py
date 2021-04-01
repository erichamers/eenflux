from django.urls import path

from .views import MyCamgaignsView, ApplicationView, ApplicationDetailsView

app_name = 'influencers'
urlpatterns = [
    path('my-proposals/', MyCamgaignsView.as_view(), name='my-proposals'),
    path('apply/<int:pk>', ApplicationView.as_view(), name='apply'),
    path('application/<int:pk>', ApplicationDetailsView.as_view(), name='application-details'),
]