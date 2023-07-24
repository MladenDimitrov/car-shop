from django.db import models
from car_shop.account.validators import check_name
from django.core.validators import MinLengthValidator
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, validators=[check_name, MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, blank=True, null=True, validators=[check_name, MinLengthValidator(1)])
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='images')
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
