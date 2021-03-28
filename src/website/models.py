from django.db import models

from accounts.models import Business, Influencer


class Campaign(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.FloatField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Application(models.Model):
    
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    terms = models.TextField(null=True)
    offer = models.FloatField()
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.influencer.user.email + ' ' + self.campaign.title
        