from django.contrib import admin
from car_shop.account.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_login', 'is_staff', 'is_superuser']
    list_filter = ['last_login']
    search_fields = ['username']
