from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import crypto
from .form import CustomForm,RegisterationForm, SubcriptionForm
from django.contrib import messages
from .models import *
from django.contrib.auth.views import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.http import HttpResponse

def home(request):
    return render(request, 'crypto/home.html')

def email(request):
    return render(request, 'crypto/email_verification.html')

def Register(request):
    try:
        code = request.POST.get('refercode')
        referred = UserMembership.objects.get(referal_code=code)
    except:
        pass
    if request.method=='POST':
        form = RegisterationForm(request.POST)
        forms = CustomForm(request.POST)
        if form.is_valid() and forms.is_valid():
            user=form.save()
            profile = forms.save(commit=False)
            profile.user=user
            try:
                profile.recommended_by = referred
            except:
                pass
            profile.save()
            return redirect('/email_verification')
            
    else:
        form = RegisterationForm()
        forms = CustomForm()
    args = {'form':form, 'forms':forms}
    return render(request, 'crypto/register.html', args)

@login_required(login_url='/login/')  
def Dashboard(request):
    return render(request, 'crypto/dashboard.html')

    
@login_required(login_url='/login/')  
def profiledetails(request):
    return render(request, 'crypto/profiledetails.html')

@login_required(login_url='/login/')
def passwordreset(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Password has been succesfully updated!')
            return redirect('/login')
            
    else:
        form =  PasswordChangeForm(request.user)
    args = {'form':form}
    return render(request, 'crypto/passwordreset.html' , args)
@login_required(login_url='/login/')
def Contract(request):

    return render(request, 'crypto/contract.html')
@csrf_exempt
def Activate(request):
    user = request.user.usermembership
    wallet = Wallet.objects.get(id=1)
    if request.method == 'POST':
        form = SubcriptionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = SubcriptionForm()
    context = {'form':form, 'wallet':wallet}
    return render(request, 'crypto/buy.html', context)

def Processing(request):
    subcription_id = request.GET.get('subcription_id')
    prices = Price.objects.filter(subcription_id=subcription_id).order_by('price')
    context = {'prices':prices}
    return render(request, 'crypto/info.html', context)

def HistoryViews(request):
    user = request.user
    details = History.objects.filter(user_id=user.id)
    args = {'details':details}
    return render(request, 'crypto/history.html', args)

def confirmation(request):
    
    return render(request, 'crypto/room.html')

def checkview(request):
    username = request.POST['username']
    room = request.POST['room_id']
    if Chatroom.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room= Chatroom.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
       
def room(request, room):
    username = request.GET.get('username')
    room_details = Chatroom.objects.all().filter(name=room)
    args = {'username':username, 'room':room, 'room_details':room_details}
    return render(request, 'crypto/chat.html', args)
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(body=message,user=username, room=room_id)
    new_message.save()
    return HttpResponse('message sucessfully sent')

def receive(request, room):
    room_detail = Chatroom.objects.get(name=room)
    message = Message.objects.filter(room=room_detail)
    return JsonResponse({'message': list(message.values())}) 




