from importlib.metadata import requires
from django.shortcuts import render

def home(request):
    
    return render(request, 'core/home.html')
