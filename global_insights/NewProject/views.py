from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about-us.html')

def contact_us(request):
    return render(request,'contact_us.html')

def service_2(request):
    return render(request,'service2.html')

def service_1(request):
    return render(request,'services.html')
