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
            request.session['name'] = request.POST['name']
            request.session['email'] =  request.POST['email']
            request.session['Gender'] =  request.POST['Gender']
            request.session['favorite_language'] =  request.POST['favorite_language']
            request.session['dojo_location'] =  request.POST['dojo_location']
            request.session['comment'] =  request.POST['comment']
            request.session['lovezak'] =  lovezak
            return redirect("/view_result" )
        else:  return HttpResponse("You can't not love Zak!")

def view_survey_result(request):
    return render(request, "result.html")