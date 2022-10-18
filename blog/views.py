from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Contact
from datetime import date, datetime
from django.contrib import messages


def home(request):
   return render(request,'index.html')


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request,'about.html')

def services(request):
    # return HttpResponse('<h1>Blog Services</h1>')
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')

        

        

    # return HttpResponse('<h1>poudelkeshav789@gmail.com</h1>')
    return render(request,'contact.html')

