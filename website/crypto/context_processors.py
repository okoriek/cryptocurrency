from .models import *
from django.contrib.auth.models import User


def notification(request):
    info =  Notification.objects.all()
    count = Notification.objects.count()
    return {'notification':info, 'number':count}

def pending(request):
    user_id = request.user
    count = 0
    if user_id.is_authenticated:
        figure = History.objects.all().filter(user = user_id).filter(status = False).count()
        count += figure
    else:
        pass
    return{'pending_request':count}

def withdrawal(request):
    total = 0 
    user_id  =  request.user
    if user_id.is_authenticated:
        withdraw = History.objects.filter(user = user_id).filter(status = True)
        amount = withdraw.values_list('payout', flat=True)
        for i in amount:
            total += float(i)
    else:
        pass
    return {'withdrawal_amount':total}

def Profit(request):
    total = 0 
    user_id = request.user
    if user_id.is_authenticated:    
        withdraw = History.objects.filter(user = user_id).filter(status = True)
        amount = withdraw.values_list('payout', flat=True)
        price = withdraw.values_list('price', flat=True)
        for i in price:
            total -= float(i)
        for i in amount:
            total += float(i)
    else:
        pass
    return {'profit_amount':total}

def Earnings(request):
    total = 0
    user_id  =  request.user
    if user_id.is_authenticated:
        member =  History.objects.filter(user =  user_id)
        amount =  member.values_list('payout', flat=True)
        for i in amount:
            total += float(i)
    else:
        pass
    return {'earnings': total}




    


