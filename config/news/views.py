from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse,HttpRequest

def kitob(request:WSGIRequest):
    return render(request,'index.html')

def kalendar(request:WSGIRequest):
    return render(request,'index2.html')

def products(request:WSGIRequest):
    return render(request,'index3.html')

def retsep(request:WSGIRequest):
    return render(request,'index4.html')

def sayt(request:WSGIRequest):
    return render(request,'index5.html')

def list(request:WSGIRequest):
    return render(request,'index6.html')

def kafe(request:WSGIRequest):
    return render(request,'index7.html')

def index8(request:WSGIRequest):
    return render(request,'index8.html')

def koleksiya(request:WSGIRequest):
    return render(request,'index9.html')

def galereya(request:WSGIRequest):
    return render(request,'index10.html')