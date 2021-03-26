from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import User, Influencer, Business

@receiver(post_save, sender=User)
def create_user_model_signal(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'IN':
            Influencer.objects.create(user=instance)
        else:
            Business.objects.create(user=instance)
            
@receiver(post_delete, sender=Influencer)
def delete_influencer_model_signal(sender, instance, using, **kwargs):
    instance.user.delete()            

@receiver(post_delete, sender=Business)
def delete_business_model_signal(sender, instance, using, **kwargs):
    instance.user.delete()