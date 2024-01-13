
# Create your views here.
from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account registered successfully')
            return redirect('register')
    else:
        register_form=forms.RegisterForm()
    return render(request,'register.html',{'form':register_form ,'type': 'Register'})

def user_login(request):
    if request.method=='POST':
        form =  AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'User logged in successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Invalid login information!') 
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form':form , 'type':'Login'})
    

@login_required   
def profile(request):
    return render(request,'profile.html')

@login_required
def edit_profile(request):
    if request.method=='POST':
        profile_form = forms.ChangeUserInfo(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Successfully updated profile')
            return redirect('profile')
    else:
        profile_form= forms.ChangeUserInfo()
    return render(request,'updateprofile.html',{'form':profile_form}) 

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'password updated successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'passchange.html',{'form':form})        
        
@login_required
def passchange_without(request):
    if request.method=='POST':
        form = SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password udated without old password')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'passchange2.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('home')
              
