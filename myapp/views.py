from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"myapp/base.html")

def child(request):
    return render(request,"child.html")

def home(request):
    return render(request,"myapp/home.html")

def sam(request):
    return render(request,"myapp/sam.html")