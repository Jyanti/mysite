from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    age = models. IntegerField(default = 0)


#google how to give a custom name for table when doing migration

#Create a user module. Post and get 
#{GET, UPDATE,DELETE} filter(id = user_id).update(name = "ggg")
                  # .filter{id = user_id}.delete()
                  
#1. set up python virtual environment 
#2. create a module
#3. create a GET and POST for GET, UPDATE,DELETE
