from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("http://127.0.0.1:8000/sign")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect("http://127.0.0.1:8000/sign")
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                messages.info(request,"user created succesfully")
                return redirect('/')
        else:
            messages.info(request,"password and confirm password doesnt match")
            return redirect("http://127.0.0.1:8000/sign")    


    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"doesnt match")
            return redirect("http://127.0.0.1:8000/signlog")
    
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
