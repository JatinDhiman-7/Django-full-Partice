from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def register_view(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid(): 
            user=form.save()
            login(request,user)
            messages.success(request,'Registration successful and logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Registration failed. Please correct the error below')
    else:
        form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_views(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username')
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('login')

@login_required(login_url='login')
def profile_view(request):
    return render(request,'accounts/dashboard.html')
