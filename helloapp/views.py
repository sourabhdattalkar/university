from django.shortcuts import render
# helloapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")
