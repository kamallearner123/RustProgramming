from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse("User registration page (to be implemented)")

def login_view(request):
    return HttpResponse("User login page (to be implemented)")

def logout_view(request):
    return HttpResponse("User logout page (to be implemented)")

def profile(request):
    return HttpResponse("User profile page (to be implemented)")