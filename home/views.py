from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    if request.user.is_anonymous:
        print("not login")
        return redirect ('/login')
    else:
        print("Login user")
    if request.method == "POST":
        email = request.POST.get('email')
        textData = request.POST.get('textdata')
        contact = Contact(email=email,textData=textData,date = datetime.today())
        contact.save()
        return render(request, 'contact.html')
    return render(request, 'contact.html')
    #return HttpResponse("This is about page")



def services(request):
    return HttpResponse("This is services page")




def login(request):
    if request.method == "POST":
        username = request.get("username")
        password = request.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            return redirect("/about")
        else:
            print("User is none")
            return render(request, 'login.html')
    return render(request, 'login.html')



def logoutUser(request):
    logout(request)
    return redirect("/login")
    

