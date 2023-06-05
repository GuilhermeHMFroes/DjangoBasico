from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def w3c(request):
    return render(request, 'w3c.html')

def HTML(request):
    return render(request, 'HTML.html')

def CSS(request):
    return render(request, 'CSS.html')

def JavaScript(request):
    return render(request, 'JavaScript.html')

def Frontend(request):
    return render(request, 'Frontend.html')

def Backend(request):
    return render(request, 'Backend.html')
