from django.shortcuts import HttpResponse, redirect 
from django.http import JsonResponse
from blogs.views import  index

def root(request):
    return redirect("/register")

def register(request):
    return HttpResponse(" placeholder for users to create a new user record.   ")

def login(request):
    return HttpResponse(" placeholder for users to log in ")

def user(request):
        return HttpResponse("  placeholder to display all the list of users later ")


def my_view(request): 
    redirect(index)