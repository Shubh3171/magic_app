from django.shortcuts import render
from website.models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is my home page")

def services(request):
    return render(request,"services.html")
    #return HttpResponse("This is my Services page")

def about(request):
    return render(request,"about.html")
    #return HttpResponse("This is my about page")

def design(request):
    return render(request,"design.html")
    #return HttpResponse("This is my home page")

def prototype(request):
    return render(request,"prototype.html")
    #return HttpResponse("This is my about page")

def cae(request):
    return render(request,"cae.html")
    #return HttpResponse("This is my about page")
def contact(request):
    return render(request,"contact.html")
    #return HttpResponse("This is my about page")

def styling(request):
    return render(request,"styling.html")

def save_styling(request):
    
    #return HttpResponse("This is my contact page")
    if request.method =="POST":
        print('---------------------------------------')
        print(request.POST)
        print('---------------------------------------')
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        purp = request.POST.get('purp')
        file2 = request.FILES.getlist("file")
        
        for f in file2:
            Styling(company = company, name= name, email = email, phone= phone, city = city, state= state, country= country, purp =purp,file = f).save() 
        return render(request,"styling.html")
    
def save_design(request):
    
    #return HttpResponse("This is my contact page")
    if request.method =="POST":
        print('---------------------------------------')
        print(request.POST)
        print('---------------------------------------')
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        purp = request.POST.get('purp')
        file2 = request.FILES.getlist("file")
        
        for f in file2:
            Design(company = company, name= name, email = email, phone= phone, city = city, state= state, country= country, purp =purp,file = f).save()
     
        return render(request,"design.html")
    
def save_prototype(request):
    
    #return HttpResponse("This is my contact page")
    if request.method =="POST":
        print('---------------------------------------')
        print(request.POST)
        print('---------------------------------------')
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        purp = request.POST.get('purp')
        file2 = request.FILES.getlist("file")
         
        for f in file2:
            Prototype(company = company, name= name, email = email, phone= phone, city = city, state= state, country= country, purp =purp,file = f).save()
        return render(request,"prototype.html")
    
def save_cae(request):
    
    #return HttpResponse("This is my contact page")
    if request.method =="POST":
        print('---------------------------------------')
        print(request.POST)
        print('---------------------------------------')
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        purp = request.POST.get('purp')
        file2 = request.FILES.getlist("file")
        

        for f in file2:
            CAE(company = company, name= name, email = email, phone= phone, city = city, state= state, country= country, purp =purp,file = f).save()
        
        return render(request,"cae.html")
    
