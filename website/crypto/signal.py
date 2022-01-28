from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from . models import Membership, History, Chatroom

@receiver(post_save, sender=Membership)
def HistorySave(sender, instance, created, **kwargs):
    if created == True:
        History.objects.create(user=instance.user, subcription=instance.subcription,
        price=instance.price, deactivate=instance.deactivated, subcribed=instance.created,payout=instance.payout)












    
    




