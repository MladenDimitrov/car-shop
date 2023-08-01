from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model
from car_shop.account.validators import check_name
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# These models are only visible for the staff.


class TelephoneNumber(models.Model):
    telephone_number = models.IntegerField()
    # Description is optional, only for the staff to know more about the number.
    # It can be used in the template if needed.
    description = models.CharField(max_length=20, blank=True, null=True)


class EmailModel(models.Model):
    email = models.EmailField(max_length=40)
    # Description is optional, only for the staff to know more about the email.
    # It can be used in the template if needed.
    description = models.CharField(max_length=20, blank=True, null=True)


class AddressModel(models.Model):
    address = models.TextField(max_length=50)
    # Description is optional, only for the staff to know more about the address.
    # It can be used in the template if needed.
    description = models.CharField(max_length=20, blank=True, null=True)


class WorkingHoursModel(models.Model):
    # Pattern for how the working days should be writen in the admin site.
    # First start with " or ' after that write the starting hour then spase and the end hour.
    # After the hours are correctly writen the user can write the starting day and the end day with space between.
    # In the end the user should end the sentence with " or '
    working_days = models.TextField(max_length=100)
    days_off = models.TextField(max_length=100)


UserModel = get_user_model()


class Person(models.Model):

    name = models.CharField(max_length=20, blank=True, null=True, validators=[check_name, MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, blank=True, null=True, validators=[check_name, MinLengthValidator(1)])
    email = models.EmailField(max_length=40, blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='profile_images')
    phone_number = PhoneNumberField(max_length=13, region='BG')
    address = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(UserModel, on_delete=models.RESTRICT, primary_key=True)
