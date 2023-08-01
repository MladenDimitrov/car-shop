from django.db import models

# Create your models here.


class BrakePads(models.Model):
    image_of_product_brake_pads = models.ImageField(blank=True, null=True, upload_to='product_images')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=15)
    manufacturer = models.CharField(max_length=10)
    width = models.IntegerField()
    height = models.IntegerField()
    price = models.IntegerField()
    commercial_number = models.IntegerField()


class BrakeRotors(models.Model):
    image_of_product_brake_rotors = models.ImageField(blank=True, null=True, upload_to='product_images')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=15)
    manufacturer = models.CharField(max_length=10)
    diameter = models.IntegerField()
    center_hole_diameter = models.IntegerField()
    number_of_holes = models.IntegerField()
    price = models.IntegerField()
    commercial_number = models.IntegerField()


class BrakeCylinder(models.Model):
    image_of_product_brake_cylinder = models.ImageField(blank=True, null=True, upload_to='product_images')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=15)
    manufacturer = models.CharField(max_length=10)
    diameter_of_piston = models.IntegerField()
    brake_system = models.CharField(max_length=15)
    price = models.IntegerField()
    commercial_number = models.IntegerField()
