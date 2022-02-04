import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from datetime import timedelta, timezone




class Wallet(models.Model):
    address = models.CharField(max_length=300)

    def __str__ (self):
        return self.address

    



class Subcription(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Price(models.Model):
    subcription = models.ForeignKey(Subcription, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__ (self):
        return str(int(self.price))

class Membership(models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE,blank=True, null=True)
    subcription = models.ForeignKey(Subcription, on_delete=models.DO_NOTHING)
    price = models.ForeignKey(Price, on_delete=models.DO_NOTHING)
    payout = models.CharField(blank=True, max_length=200)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.datetime.now)
    deactivated = models.DateTimeField( blank=True)
    active = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        value = datetime.datetime.now() + datetime.timedelta(days=14)
        if self.created:
            self.deactivated = value
            self.payout= int(str(self.price))*0.3 + int(str(self.price))
            self.active=True
        super().save(*args, **kwargs)


class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    recommended_by =models.CharField(max_length=200, blank=True)
    is_verified = models.BooleanField(default=False)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True,blank=True)
    wallet = models.CharField(verbose_name='wallet address',max_length=50, blank=True)
    referal_code = models.CharField(default=get_random_string(length=6), unique=True, max_length=6, blank=True)

    
    def __str__(self):
        return  str(self.user)

    
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    subcription = models.CharField(max_length=50,blank=True, null=True)
    price  = models.CharField(max_length=40, blank=True, null=True)
    payout = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=False)
    subcribed = models.DateTimeField(blank=True,null=True)
    deactivate = models.DateTimeField( blank=True, null=True)

    class Meta:
        verbose_name_plural="Histories"

    def __str__(self):
        return str(self.user)+ ' ' + str(self.pk) 

class Notification(models.Model):
    messages = models.TextField(blank=True, null=True)
    date_created = models.DateField(default=datetime.datetime.now)
    time_created = models.TimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.date_created) + ' ' + str(self.time_created)

class Chatroom(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    body = models.CharField(max_length=400000)
    date_created = models.DateField(default=datetime.datetime.now)
    time_created = models.TimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.user 


    




   
        
    

    
    


    


