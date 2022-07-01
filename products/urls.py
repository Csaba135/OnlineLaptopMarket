from django.urls import path, include
from . import views
from products.views import get_all_products, get_product

urlpatterns=[
    path('home/', views.home),
    path('allproducts/', get_all_products, name='all_products'),
    path('<int:product_id>/', get_product, name='product_details'),
]

