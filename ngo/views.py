from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from .models import Ngos
# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')

def handlesignup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password == password2:
            if Ngos.objects.filter(username=username).exists():
                print("username already exist")
                return redirect('/ngo/signup')
            elif Ngos.objects.filter(email=email).exists():
                print("email already exist")
                return redirect('/ngo/signup')
            newngo = Ngos(name=name, email=email, username=username,password =password)
            newngo.save()
            thank = True
            return render(request, 'ngo/home.html', {'thank': thank})
    return render(request, 'ngo/signup.html', {'thank': thank})

def handlelogin(request):
    if request.method=="POST":
        current_ngo = request.POST.get("username")
        password = request.POST.get("password")
        print(current_ngo)
        ngo = Ngos.objects.get(username=current_ngo)
        if ngo is not None:
            if ngo.password == password:
                print("success")
                return render(request, 'ngo/home.html')
        return render(request, 'login.html')
    return render(request, 'login.html')