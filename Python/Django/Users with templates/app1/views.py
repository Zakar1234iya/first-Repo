from django.shortcuts import *
from . import models

def index(request):
    context = { 
    'users' : models.get_all_users()
    }
    
    return render( request, 'index.html' , context )

def create_new_user(request):
    models.create_user(request.POST)
    return redirect('/')