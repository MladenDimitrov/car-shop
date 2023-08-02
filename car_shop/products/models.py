from django.db import models

# Create your models here.


class BrakePads(models.Model):
    image_of_product_brake_pads = models.ImageField(blank=True, null=True, upload_to='product_images/brake_parts/pads')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    width = models.IntegerField()
    height = models.IntegerField()
    price = models.IntegerField()
    commercial_number = models.CharField()


class BrakeRotors(models.Model):
    image_of_product_brake_rotors = models.ImageField(blank=True, null=True, upload_to='product_images/brake_parts/rotors')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    diameter = models.IntegerField()
    number_of_holes = models.IntegerField()
    price = models.IntegerField()
    commercial_number = models.CharField()


class BrakeCylinder(models.Model):
    image_of_product_brake_cylinder = models.ImageField(blank=True, null=True, upload_to='product_images/brake_parts/cylinder')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    diameter_of_piston = models.IntegerField()
    brake_system = models.CharField(max_length=30)
    price = models.IntegerField()
    commercial_number = models.CharField()


class EngineValves(models.Model):
    image_of_product_engine_valve = models.ImageField(blank=True, null=True, upload_to='product_images/engine_parts/valve')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    type_of_valve = models.CharField(max_length=30)
    type_of_exploitation = models.CharField(max_length=30)
    operating_current = models.IntegerField()
    price = models.IntegerField()


class EngineChainDrive(models.Model):
    image_of_product_engine_chain_drive = models.ImageField(blank=True, null=True, upload_to='product_images/engine_parts/chain_drive')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    price = models.IntegerField()


# class CamshaftPulley(models.Model):
#     image_of_product_engine_cam_shaft_pulley = models.ImageField(blank=True, null=True, upload_to='product_images/engine_parts/cam_shaft_pulley')
#     for_car = models.CharField(max_length=30)
#     engine = models.CharField(max_length=30)
#     batch_number = models.CharField(max_length=30)
#     manufacturer = models.CharField(max_length=30)
#     length = models.IntegerField()
#     size_of_outside_carving = models.IntegerField()
#     size_of_outside_carving = models.CharField()
#     size_of_key = models.IntegerField()
#     type_of_exploitation = models.CharField(max_length=30)
#     weight = models.IntegerField()
#     price = models.IntegerField()
# after changing the size_of_outside_carving and making migration and migrate the web app started to show me one error
# the error was that I wasn't providing the correct data to this field, but the data was correct
# after I dump the table in the database I run again the make migration and migrate commands but in the database
# no table show up after migration.
# server error 500


class DriveTrainSemiAxleBox(models.Model):
    image_of_product_drivetrain_semi_axle_box = models.ImageField(blank=True, null=True, upload_to='product_images/drivetrain_parts/semi_axle_box')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    type_of_transmission = models.CharField(max_length=30)
    side_of_mounting = models.CharField(max_length=30)
    driving_axis = models.CharField(max_length=30)
    length = models.IntegerField()
    surface = models.CharField(max_length=30)
    price = models.IntegerField()


class DriveTrainHalfAxle(models.Model):
    image_of_product_drivetrain_half_axle = models.ImageField(blank=True, null=True, upload_to='product_images/drivetrain_parts/half_axle')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    type_of_transmission = models.CharField(max_length=30)
    side_of_mounting = models.CharField(max_length=30)
    abs_ring = models.IntegerField()
    count_of_abs_rings = models.IntegerField()
    length = models.IntegerField()
    type_of_carving = models.CharField(max_length=30)
    number_of_holes = models.IntegerField()
    price = models.IntegerField()


class DriveTrainDriveShaft(models.Model):
    image_of_product_drivetrain_drive_shaft = models.ImageField(blank=True, null=True, upload_to='product_images/drivetrain_parts/drive_shaft')
    for_car = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    side_of_mounting = models.CharField(max_length=30)
    length = models.IntegerField()
    production_number = models.CharField()
    price = models.IntegerField()
