from django.db import models

from accounts.models import User

class Business(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Businesses'
    
    def __str__(self):
        return self.user.email