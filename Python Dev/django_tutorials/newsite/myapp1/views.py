from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    # return HttpResponse("I an about")
    return render(request,"about.html")