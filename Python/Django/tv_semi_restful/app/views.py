from django.shortcuts import render, redirect, get_object_or_404
from .models import Show
from django.contrib import messages

def index(request):
    return redirect("/shows")

def show_all(request):
    context = {'shows': Show.display_all()}
    return render(request, "index.html", context)

def add_new(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            Show.create_show(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST.get('description', '')
            )
            return redirect("/shows")
    return render(request, "add_show.html")

def create_new(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            new_show = Show.create_show(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST.get('description', '')
            )
            return redirect(f"/shows/{new_show.id}")
    return redirect("/shows/new")

def view_show(request, id):
    show = Show.get_show_by_id(id)
    return render(request, "shows_info.html", {'show': show})

def edit_show(request, id):
    show = Show.get_show_by_id(id)
    if request.method == "POST":
        title = request.POST.get('title', '')
        network = request.POST.get('network', '')
        release_date = request.POST.get('release_date', '')
        description = request.POST.get('description', '')

        errors = Show.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit')
        else:
            if title and network and release_date and description:
                Show.update_show(
                    id=id,
                    title=title,
                    network=network,
                    release_date=release_date,
                    description=description
                )
                return redirect(f"/shows/{id}")
            else:
                messages.error(request, "All fields are required.")
                return render(request, "edit_show.html", {"show": show})
    
    return render(request, "edit_show.html", {'show': show})


def update_show(request, id):
    if request.method == "POST":
        Show.update_show(
            id=id,
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST.get('description', '')
        )
        return redirect(f"/shows/{id}")
    return redirect(f"/shows/{id}/edit")

def delete_show(request, id):
    Show.delete_show(id)
    return redirect("/shows")




