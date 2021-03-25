from django.db import models

from accounts.models import Business

class Campaign(models.Model):

    title = models.CharField(max_length=200)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title