from django.contrib import admin
from . models import  Chatroom, Message, History, Membership, Notification, UserMembership, Price, Subcription, Wallet

admin.site.register(Membership)
admin.site.register(UserMembership)
admin.site.register(Wallet)
admin.site.register(Price)
admin.site.register(Subcription)
admin.site.register(History)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(Chatroom)




