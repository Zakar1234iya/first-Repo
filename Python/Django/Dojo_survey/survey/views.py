from django.shortcuts import  * 
from django.http import * 

def root(request):
    return redirect("/")
def index(request):
    return render(request, 'index.html')
def survey_result(request):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        lovezak = 'yes' if request.POST.get('lovezak') == 'yes' else 'no'
        if lovezak=='yes':
            context = {
                "name" : request.POST['name'],
                "email" : request.POST['email'],
                "Gender" : request.POST['Gender'],
                "favorite_language" : request.POST['favorite_language'],
                "dojo_location" : request.POST['dojo_location'],
                "comment" : request.POST['comment'],
                "lovezak": lovezak

            }
            return render(request ,"result.html" , context)
        else:  return HttpResponse("You can't not love Zak!")

    