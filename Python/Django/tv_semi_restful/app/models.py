from django.db import models
from django.utils import timezone

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def display_all():
        return Show.objects.all()

    def get_show_by_id(id):
        return Show.objects.get(id=id)

    def create_show(title, network, release_date, description):
        Show.objects.create(title=title, network=network, release_date=release_date, description=description)

    def update_show(id, title, network, release_date, description):
        show = Show.objects.get(id=id)
        show.title = title
        show.network = network
        show.release_date = release_date
        show.description = description
        show.save()
        return show

    def delete_show(id):
        show = Show.objects.get(id=id)
        show.delete()
