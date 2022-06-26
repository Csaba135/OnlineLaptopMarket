from django.contrib import admin
from products.models import Store, Product, WishList

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(WishList)
class StoreAdmin(admin.ModelAdmin):
    pass