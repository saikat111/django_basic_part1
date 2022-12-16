from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    if request.method == "POST":
        email = request.POST.get('email')
        textData = request.POST.get('textdata')
        contact = Contact(email=email,textData=textData,date = datetime.today())
        contact.save()
    return render(request, 'contact.html')
    #return HttpResponse("This is about page")



def services(request):
    return HttpResponse("This is services page")

