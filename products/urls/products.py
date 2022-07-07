from django.urls import path, include
from products.views.products import get_all_products, get_product, wishlist, delete_from_wishlist

app_name = 'products'

urlpatterns = [
    path('', get_all_products, name='all_products'),  # /products
    # path('<int:product_id>/add_to_cart', add_to_cart, name='add_to_cart'),  # /products/<product_id>
    path('wishlist/', wishlist, name='wishlist'),  # /products/<product_id>
    path('<int:product_id>/', get_product, name='product_details'),  # /products/<product_id>
    path('delete_from_wishlist_<int:product_id>/', delete_from_wishlist, name='delete_from_wishlist'),  # /products/<product_id>
    # path('<int:product_id>/like/', like_product, name='like'),  # /products/<product_id>/like
]