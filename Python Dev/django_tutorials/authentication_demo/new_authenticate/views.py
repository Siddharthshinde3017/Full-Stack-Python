# from Demos.win32ts_logoff_disconnected import username
from Demos.win32ts_logoff_disconnected import username
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def formsave(request):
    return render(request,'formsave.html')

def formcheck(request):
    if request.method=='POST':
        fn= request.POST['first_name']
        ln= request.POST['last_name']
        em = request.POST['username']
        ps = request.POST['password']

        u1 = User.objects.create_user(first_name = fn,last_name= ln,username=em,password=ps)
        u1.save()
        return HttpResponse("successful")
    else:
        return HttpResponse("failed")

def signin(request):
     return render(request,"signin.html")
def dashboard(request):
    return render(request,"dashboard.html")

def signcheck(request):
    if request.method == 'POST':
        un = request.POST['username']
        ps = request.POST['password']

        data = authenticate(username= un, password=ps)
        if data:
            login(request,data)
            return redirect("/dashboard")
        else:
            return HttpResponse("failed ")
    else:
        return HttpResponse("failed")
def signout(request):
    logout(request)
    return redirect("/signin")

def resetpassword(request):
    return render(request,"resetpassword.html")

def reset(request):
    if request.method == 'POST':
        un = request.POST['username']
        op = request.POST['old_password']
        np = request.POST['new_password']
        data = authenticate(username = un,password = op, new_password = np)

        if data:
            data.set_password(np)
            data.save()

            return HttpResponse("reset sucessful")
        else:
            return HttpResponse("failed to rest")
    else:
        return HttpResponse("failed")