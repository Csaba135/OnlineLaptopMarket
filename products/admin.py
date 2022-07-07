from django.contrib import admin
from django.utils.html import format_html
from products.models import Store, Product, WishList, NotificationAboutProduct

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    @admin.display(description='Image')
    def logo_html(self, obj):
        return format_html(f'<img src="{obj.logo_url}" width="50" />')

    def products(self, obj):
        products = Product.objects.filter(store=obj.store_id_s)
        return len(products)

    list_display = ('name', 'logo_html', 'products')

@admin.register(Product)
class StoreAdmin(admin.ModelAdmin):
    @admin.display(description='Image')
    def image_html(self, obj):
        return format_html(f'<img src="{obj.image_url}" width="50" />')

    list_display = ('title', 'store', 'image_html')

