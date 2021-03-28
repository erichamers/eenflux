from django import forms

from .models import Campaign, Application


class CreateCampaignForm(forms.ModelForm):
    
    class Meta:
        model = Campaign
        fields = ('title', 'description', 'budget')


class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = ('offer', 'terms')