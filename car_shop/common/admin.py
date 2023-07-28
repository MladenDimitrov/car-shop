from django.contrib import admin

from car_shop.common.models import Person


# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
