from products.models import Store, Product
from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator

def get_all_stores(request):
    stores = Store.objects.all()

    return render(request, 'products/stores.html', {
        "stores": stores,
    })
def get_products_from_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(store_id=store.id).all

    return render(request, 'products/store.html', {
        "products": products,
        "store":store,
    })
