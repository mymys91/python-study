from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'hausdj23@aey'})

def password(request):
    thepassword = ''    
    characters = list('abcdefhijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('^#$!'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    nlength = int(request.GET.get('length'))
    for x in range(nlength):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')