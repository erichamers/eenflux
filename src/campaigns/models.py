from django.db import models

from businesses.models import Business
from influencers.models import Influencer

class Campaign(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField()
    budget = models.FloatField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    ongoing = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

    @property
    def is_active(self):
        return self.ongoing
    
    def finish_campaign(self):
        self.ongoing = False
    

class Application(models.Model):
    
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    terms = models.TextField(null=True)
    offer = models.FloatField()
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.influencer.user.email + ' ' + self.campaign.title
    
    @property
    def been_accepted(self):
        return self.accepted
    
    @property
    def been_rejected(self):
        return self.rejected
