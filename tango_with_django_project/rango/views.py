from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #construct a dictionary to pass to template as its content
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
     context_dict = {'boldmessage': 'This tutorial has been put together by qinwen'}
     return render(request, 'rango/about.html', context = context_dict)