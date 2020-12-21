from django.shortcuts import render
from django.http import HttpResponse # Responsible for returning a response to a user.

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Kibera Times')