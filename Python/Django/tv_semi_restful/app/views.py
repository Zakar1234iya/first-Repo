from django.shortcuts import render, redirect, get_object_or_404
from .models import Show

def index(request):
    return redirect("/shows")

def show_all(request):
    context = {
        'shows': Show.display_all()
    }
    return render(request, "index.html", context)

def add_new(request):
    if request.method == "POST":
        Show.create_show(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect("/shows")
    return render(request, "add_show.html")

def create_new(request):
    if request.method == "POST":
        Show.create_show(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect("/shows")
    return redirect("/shows/new")


def view_show(request, id):
    show = Show.objects.get(id=id)
    return render(request, "shows_info.html", {'show': show})


def edit_show(request, id):
    show = Show.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        network = request.POST.get('network')
        release_date = request.POST.get('release_date')
        description = request.POST.get('description')
        
        if title and network and release_date and description:  # Ensure none are None
            show.title = title
            show.network = network
            show.release_date = release_date
            show.description = description
            show.save()
            return redirect(f"/shows/{id}")
        else:
            # Handle the case where one or more fields are missing
            return render(request, "edit_show.html", {"show": show, "error": "All fields are required."})
    
    context = {'show': show}
    return render(request, "edit_show.html", context)



def update_show(request, id):
    if request.method == "POST":
        Show.update_show(
            id=id,
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect(f"/shows/{id}")
    return redirect(f"/shows/{id}/edit")

def delete_show(request, id):
    Show.delete_show(id)
    return redirect("/shows")
