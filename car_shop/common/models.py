from django.db import models

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
