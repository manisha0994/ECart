from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (Request):
    return render(Request, 'Shop/index.html')

def about(Request):
    return HttpResponse('Welcome Back in About page')

def contact(Request):
    return HttpResponse('Welcome Back in contact page')

def tracker(Request):
    return HttpResponse('Welcome Back in tracker page')

def search(Request):
    return HttpResponse('Welcome Back in search page')

def productView(Request):
    return HttpResponse('Welcome Back in productView page')

def CheckOut(Request):
    return HttpResponse('Welcome Back in CheckOut page')