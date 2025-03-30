import re
from django.shortcuts import render,redirect
from .models import Account



def login(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        if not Account.objects.filter(email=email).exists():
            return render(request,'login.html',{'message':'Email not registered'})
        if Account.objects.filter(email=email,password=password):
            return redirect('home')
    return render(request,'login.html')



def register(request):
    if request.method =='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        if Account.objects.filter(email=email).exists():
            return render(request,'register.html',{'message':'Email already registered'})
        user=Account.objects.create(firstName=firstName,lastName=lastName,email=email,phone=phone,password=password)
        user.save()
        return redirect('login')
    return render(request,'register.html')
    



def logout(request):
    return render(request,'register.html')