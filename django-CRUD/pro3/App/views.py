from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from App.form import *
from App.models import *
# Create your views here.
def home(request):
    return render(request,'base.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'Username is already exits!!!!')
                print("Already have ")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                print("success")
                return redirect(user_login)
        else:
            print(" Wrong Password")
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            messages.info(request,'User Not Exist')
            print("User Not Exist")
            return redirect(user_login)
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(user_login)

def Add(request):
    if request.method=='POST':
        form=bookform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'Add.html')
def list(request):
    d=book.objects.all()
    return render(request,'list.html',{'book':d})
def delete_item(request,a):
    m=book.objects.get(pk=a)
    m.delete()
    return render(request,'home.html',{'book':m})

        

