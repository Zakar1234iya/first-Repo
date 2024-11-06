from django.shortcuts import *

def index(request):
    return HttpResponse("response from index method from root route, localhost:8000!")