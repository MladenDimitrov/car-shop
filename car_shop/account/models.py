from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    profile_photo = models.ImageField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
