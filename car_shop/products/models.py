from django.db import models


class Products(models.Model):
    BRAKING_SYSTEM = 'BS'
    DRIVETRAIN = 'DT'
    ENGINE = 'EN'
    CATEGORY_OF_PRODUCT = [
        (BRAKING_SYSTEM, 'Braking system'),
        (DRIVETRAIN, 'Drivetrain'),
        (ENGINE, 'Engine')
    ]
    BRAKING_PADS = 'BP'
    BRAKING_ROTORS = 'BR'
    BRAKING_CYLINDERS = 'BC'
    DRIVETRAIN_SEMI_AXLE_BOX = 'DSA'
    DRIVETRAIN_DRIVE_SHAFT = 'DDS'
    DRIVETRAIN_HALF_AXLE = 'DHA'
    ENGINE_VALVES = 'EV'
    ENGINE_CHAIN_DRIVE = 'ECD'
    ENGINE_CAM_SHAFT_PULLEY = 'ECP'
    TYPE_OF_PRODUCT = [
        (BRAKING_PADS, 'Braking pads'),
        (BRAKING_ROTORS, 'Braking rotors'),
        (BRAKING_CYLINDERS, 'Braking cylinders'),
        (DRIVETRAIN_SEMI_AXLE_BOX, 'Drivetrain semi axle box'),
        (DRIVETRAIN_DRIVE_SHAFT, 'Drivetrain drive shaft'),
        (DRIVETRAIN_HALF_AXLE, 'Drivetrain half axle'),
        (ENGINE_VALVES, 'Engine valves'),
        (ENGINE_CHAIN_DRIVE, 'Engine chain drive'),
        (ENGINE_CAM_SHAFT_PULLEY, 'Engine cam shaft pulley')
    ]

    image_of_the_product = models.ImageField(upload_to='product_images')
    for_car = models.CharField(max_length=50)
    engine = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    # When writing specifications of the product you should follow specific pattern
    # Example
    # Diameter: 120mm
    # Operating current: 12V and so on ...
    specifications = models.CharField(max_length=500)
    category_of_product = models.CharField(choices=CATEGORY_OF_PRODUCT)
    type_of_product = models.CharField(choices=TYPE_OF_PRODUCT)
    price = models.IntegerField()
