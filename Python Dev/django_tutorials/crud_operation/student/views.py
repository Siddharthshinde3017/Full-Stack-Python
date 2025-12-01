
from django.shortcuts import render, HttpResponse, redirect
# from docutils.nodes import address
# from fontTools.misc.cython import returns

from  .models import student


# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    if request.method == "POST":
        n1 = request.POST["num1"]
        n2 = request.POST["num2"]

        result = int(n1)+int(n2)
        return HttpResponse(f"addition={result}")
    else:
        return HttpResponse("failed")

def registration(request):
    return render(request,"registration.html")

def saveform1(request):
    if request.method=="POST":
        fn = request.POST["fullname"]
        em = request.POST["email"]
        ct =request.POST["contact"]
        ps = request.POST["password"]
        ad = request.POST["address"]

        s= student(fullname=fn,email=em,contact=ct,password=ps,address=ad)
        s.save()

        return redirect("/welcome")
    else:
        return redirect("/registration")

def welcome(request):
    data = student.objects.all().order_by("-id")            #select * from
    return render(request,"welcome.html",{'data':data})         #in flask data = data

def deletestudent(request,id):
    student.objects.filter(id=id).delete()      #calls delete from student where id = id
    return redirect("/welcome")

def edit(request,id):
    data = student.objects.all().filter(id=id)
    return render(request,"update_form.html",{'data':data})

def update_form(request):
    if request.method=="POST":
        id = request.POST["id"]
        fn = request.POST["fullname"]
        em = request.POST["email"]
        cn = request.POST["contact"]
        ps = request.POST["password"]
        ad = request.POST["address"]

        student.objects.filter(id=id).update(fullname=fn,email= em,contact = cn,password=ps,address=ad)
        return redirect("/welcome")
    else:
        return redirect("/welcome")


def login(request):
    return render(request,"login.html")

def check_login(request):
    if request.method=="POST":
        em = request.POST["email"]
        ps = request.POST["password"]

        data= student.objects.filter(email= em,password=ps)
        if data:
            return redirect("/Dashboard")
        else:
             return redirect("/login")
    else:
        return HttpResponse("failed")


def Dashboard(request):
    return render (request,"Dashboard.html")

def logout(request):
    return redirect("/login")

