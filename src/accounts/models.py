from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    
    email = models.EmailField(max_length=200, unique=True)
    is_admin = models.BooleanField(default=False)
    user_type = models.CharField(
        max_length=3,
        choices=[
            ('BZ', 'Business'),
            ('IN', 'Influencer'),
        ],
        blank=False,
    )   
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_business(self):
        if self.user_type == 'BZ':
            return True
        else:
            return False
    
    
class Business(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Businesses'
    
    def __str__(self):
        return self.user.email
    

class Influencer(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.email
