from django.contrib import admin
from car_shop.products.models import (BrakePads, BrakeRotors, BrakeCylinder, EngineValves, EngineChainDrive,
                                      DriveTrainSemiAxleBox, DriveTrainHalfAxle, DriveTrainDriveShaft)


@admin.register(BrakePads)
class BrakePadsAdmin(admin.ModelAdmin):
    pass


@admin.register(BrakeRotors)
class BrakeRotorsAdmin(admin.ModelAdmin):
    pass


@admin.register(BrakeCylinder)
class BrakeCylinderAdmin(admin.ModelAdmin):
    pass


@admin.register(EngineValves)
class EngineValvesAdmin(admin.ModelAdmin):
    pass


@admin.register(EngineChainDrive)
class EngineChainDriveAdmin(admin.ModelAdmin):
    pass


@admin.register(DriveTrainSemiAxleBox)
class DriveTrainSemiAxleBoxAdmin(admin.ModelAdmin):
    pass


@admin.register(DriveTrainHalfAxle)
class DriveTrainHalfAxleAdmin(admin.ModelAdmin):
    pass


@admin.register(DriveTrainDriveShaft)
class DriveTrainDriveShaftAdmin(admin.ModelAdmin):
    pass
