from django.shortcuts import render

def application(request):
    return render(request, 'application.html')

def home(request):
    return render(request, 'home.html')

# Create your views here.
