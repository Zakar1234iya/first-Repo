from django.shortcuts import *
from . import models
from .models import Dojo, Ninja

def index(request):
    context = {
        'dojos' : models.diplay_dojo(),
        'ninjas' : models.display_ninja(),
    }
    return render( request, 'index.html' , context )


def create_new_dojo(request):
    models.create_dojo(request.POST)
    return redirect('/')

def create_new_ninja(request):
    models.create_ninja(request.POST)
    return redirect('/')

def delete_dojo(request, dojo_id): 
    z = Dojo.objects.get(id=dojo_id)
    z.delete_dojo() 
    return redirect('/')


