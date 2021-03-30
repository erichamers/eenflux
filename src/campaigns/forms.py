from django import forms

from campaigns.models import Campaign, Application

class CampaignForm(forms.ModelForm):
    
    description = forms.CharField(strip=False, widget=forms.Textarea)
    
    class Meta:
        model = Campaign
        fields = ('title', 'description', 'budget')
        
        
class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = ('offer', 'terms')