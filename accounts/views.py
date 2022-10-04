from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import DsaUser
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

#utilities
def get_user_list():
    user_list = []
    dsa_users = User.objects.all()
    for user in dsa_users:
        print(user.username)
        user_list.append(user.username)
    return user_list

def get_email_list():
    email_list = []
    for user in User.objects.all():
        email_list.append(user.email)
    return email_list

# Create your views here.
def register(request):
    context = {}
    if 'register' in request.POST:
        # register btn clicked
        user = User()
        if 'username' in request.POST:
            user.username = request.POST.get('username')
            if user.username in get_user_list():
                messages.error(request,message = 'Username already registered')
                return render(request,'accounts/register.html',context)
            if 'password' in request.POST:
                user.set_password(request.POST.get('password'))
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.email = request.POST.get('email')
                if user.email in get_email_list():
                    messages.error(request,"Email has already been used, please try logging in or using another email id.")
                    return render(request,"accounts/register.html",context)
                try:
                    user.save()
                except:
                    messages.error(request,"Not able to create user")
                    return render(request,"accounts/register.html",context)
                new_dsa_user = DsaUser()
                new_dsa_user.user = user
                new_dsa_user.save()
                messages.success(request,"User "+user.username+" has been succefully registered.")
                return redirect('/accounts/login')
    return render(request,'accounts/register.html',context)

def login_view(request):
    context = {}
    if 'login' in request.POST:
        # login btn pressed
        # check if user with given username exists
        user_requested = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user_requested is None:
            messages.info(request,"User doesn't exist")
        else:
            dsa_user = DsaUser.objects.filter(user__username = user_requested.get_username())
            if len(dsa_user) > 0:
                auth.login(request,user_requested)
                messages.success(request,"Login Successful")
                return redirect('/')
            else:
                messages.info(request,"User has account as an admin please login from there.")
    return render(request,'accounts/login.html',context)

@login_required
def logout_page(request):
    # print("request.user")
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request,'User logged out successfully')
        return redirect('/accounts/login')
    return redirect('/accounts/login')