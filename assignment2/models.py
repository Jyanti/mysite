#from . import models
from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    age = models. IntegerField(default = 0)
