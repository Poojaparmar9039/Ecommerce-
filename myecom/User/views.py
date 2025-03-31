import random
import re
from django import conf
from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth.hashers import make_password, check_password
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Account.objects.get(email=email)  
        except Account.DoesNotExist:
            return render(request, 'login.html', {'message': 'Email not registered'})
        if check_password(password, user.password): 
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return render(request, 'login.html', {'message': 'Invalid credentials'})
    return render(request, 'login.html')

def forgot_password(request):
    return render(request, 'forgot.html')

def send_otp(request):
    if request.method =='POST':
        email=request.POST.get('email')
        if Account.objects.filter(email=email).exists():
            otp= str(random.randint(100000, 999999))
            subject = 'Your OTP Code'
            message = f'Your OTP code is {otp}'
            email_from = EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            request.session['otp'] = otp
            request.session['email'] = email
            return render(request, 'verifyOtp.html')
    return render(request, 'forgot.html',{'message':'Email not registered'})


def verifyOtp(request):
    if request.method=='POST':
        userotp=request.POST.get('userotp')
        stored_otp=request.session.get('otp')
        
        if stored_otp==userotp:
            userotp=None
            del request.session['otp']
            return render(request,'change_password.html')
    return render(request, 'verifyOtp.html')

def register(request):
    if request.method =='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        hashed_password = make_password(password)
        if Account.objects.filter(email=email).exists():
            return render(request,'register.html',{'message':'Email already registered'})
        user=Account.objects.create(firstName=firstName,lastName=lastName,email=email,phone=phone,password=hashed_password)
        user.save()
        return redirect('login')
    return render(request,'register.html')
    

def logout(request):
    request.session.flush()  
    return redirect('login')




def change_password(request):
    if request.method =='POST':
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        if new_password != confirm_password:
            return render(request,'change_password.html',{'error':'Password not matched'})
        email=request.session.get('email')
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email=email)
            user.password=make_password(new_password)
            print(user.password)
            user.save()
            return redirect('login')
    return render(request,'change_password.html',{'error':'Not changed'})
            
