from django.shortcuts import  * 
from django.http import * 
from datetime import *


def index(request):
    return redirect("/time_display")
def time_display(request):
    now = datetime.now()
    context = {
        'now': now,
        'date_time': now.strftime("%b %d %Y %I:%M:%S %p"),
    }
    return render(request , "time_display.html" , context)


