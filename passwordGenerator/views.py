from django.shortcuts import render
## HttpResponse package helps django to provide data to the request created by user
from django.http import HttpResponse
## random module to generate random numbers
import random

# Create your views here.
## Views can be created by creating a definition and passing an argument 'request'
def home(request):
    ## render method helps the view to access the templates using
    ## following syntax 
    return render(request,'passwordGenerator/index.html')

def password(request):
    ## Variable definition
    randomPassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')


    ## request.GET.get() method access the name from the html tags
    ## 12 is the default value
    length = int(request.GET.get('length',12))

    ## if uppercase checkbox is selected
    ## Uppercase characters will be added to characters list
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    ## if special checkbox is selected
    ## special characters will be added to characters list
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    ## if numbers checkbox is selected
    ## numbers will be added to characters list
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    

    for num in range(length):
        randomPassword += random.choice(characters)

    return render(request , 'passwordGenerator/password.html',{'password':randomPassword})


def aboutus(request):
    return render(request , 'passwordGenerator/aboutus.html')