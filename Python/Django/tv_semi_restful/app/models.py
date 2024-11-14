from django.db import models
from django.utils import timezone



class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        title = postData.get('title', '')
        network = postData.get('network', '')
        release_date = postData.get('release_date', '')
        description = postData.get('description', '')

        if len(title) < 2:
            errors["title"] = "Title should be at least 5 characters"
        if len(network) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if release_date:
            release_date = timezone.datetime.strptime(release_date, '%Y-%m-%d').date()
            if release_date >= timezone.now().date():
                errors["release_date"] = "Release date should be in the past"
        if description and len(description) < 10:
            errors["description"] = "Description should be at least 10 characters if provided"
        if Show.objects.filter(title=title).exists():
            errors["title"] = "A show with this title already exists"

        return errors
        
class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
    
    
    
    def display_all():
        return Show.objects.all()

    def get_show_by_id(id):
        return Show.objects.get(id=id)

    def create_show(title, network, release_date, description): 
        show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        return show

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


