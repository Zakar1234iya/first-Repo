from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return HttpResponse("placeholder to display all the surveys created.")

def index(request):
    return HttpResponse(" placeholder for users to add a new survey ")

