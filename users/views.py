from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login ,logout ,authenticate
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")

def login_view(request):
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        user = authenticate(request,username = user,password = passw)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request , "users/login.html",{
                "message" : "Invalid"
            })
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"Logout"
    })