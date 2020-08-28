from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'passwordGenerator/index.html')

def password(request):
   
    randomPassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')


    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    

    for num in range(length):
        randomPassword += random.choice(characters)

    return render(request , 'passwordGenerator/password.html',{'password':randomPassword})


