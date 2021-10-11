from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registration(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    # password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
 

class User(models.Model):
    pass