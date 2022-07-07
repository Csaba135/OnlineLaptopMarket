from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Customer, AuthUser

@admin.register(Customer)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "nationality", "date_of_birth")

@admin.register(AuthUser)
class StoreAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("email", "first_name", "last_name", "is_staff")