from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField(2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



def create_user(data):
    User.objects.create(first_name=data['fname'], last_name=data['lname'],email_address=data["email"], age = data["age"])
    
def get_all_users():
    users = User.objects.all()
    return users

    