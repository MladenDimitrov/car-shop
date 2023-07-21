from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    profile_photo = models.ImageField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
