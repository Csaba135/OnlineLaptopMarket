from django.contrib import admin
from users.models import Customer

@admin.register(Customer)
class StoreAdmin(admin.ModelAdmin):
    pass


