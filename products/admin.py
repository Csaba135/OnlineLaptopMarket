from django.contrib import admin
from products.models import Store, Product, WishList, NotificationAboutProduct

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(WishList)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(NotificationAboutProduct)
class StoreAdmin(admin.ModelAdmin):
    pass