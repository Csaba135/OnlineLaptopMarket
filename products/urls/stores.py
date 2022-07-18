from django.urls import path
from products.views.stores import get_all_stores, get_products_from_store

app_name = 'stores'

urlpatterns = [
    path('', get_all_stores, name='all_stores'),
    path('<int:store_id>/', get_products_from_store, name='all_products_from_store'),
]