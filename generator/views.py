from django.http.response import HttpResponse
from django.shortcuts import render # its helpfull to pass a template
from django.http import HttpResponse
import random 
def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_-=+'))
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    length=int(request.GET.get('length',12)) # we will do casting ,12 is the defualt number 
    thenewpass = ''
    for i in range(length):
        thenewpass += random.choice(characters)
    return render(request,'generator/password.html',{'password':thenewpass}) 

def about(request):
    return render(request,'generator/about.html')