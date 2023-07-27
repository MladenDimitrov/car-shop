from django.contrib import admin
from car_shop.account.models import AppUser
# Register your models here.


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     pass


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass
