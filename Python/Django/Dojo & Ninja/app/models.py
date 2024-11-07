from django.db import models


class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")
    
    def delete_dojo(self): 
        self.delete()


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    
    
    
def diplay_dojo():
    return Dojo.objects.all()
    
def display_ninja():
    return Ninja.objects.all()
    
def create_dojo(data1):
    Dojo.objects.create(name=data1['name'], city=data1['city'],state=data1["state"])
    
def create_ninja(data2):
    dojo = Dojo.objects.get(id=data2['dojo'])
    Ninja.objects.create(first_name=data2['fname'],last_name=data2['lname'], dojo=dojo)
    
