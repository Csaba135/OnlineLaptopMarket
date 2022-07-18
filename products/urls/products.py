from django.urls import path
from products.views.products import get_all_products, get_product, wishlist, delete_from_wishlist

app_name = 'products'

urlpatterns = [
    path('', get_all_products, name='all_products'),
    path('wishlist/', wishlist, name='wishlist'),
    path('<int:product_id>/', get_product, name='product_details'),
    path('delete_from_wishlist_<int:product_id>/', delete_from_wishlist, name='delete_from_wishlist'),
]