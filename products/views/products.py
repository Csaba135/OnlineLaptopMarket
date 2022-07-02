from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator

def home(request):
    return render(request, 'products/home.html')

def get_all_products(request):
    products = Product.objects.order_by('price').all()

    return render(request, 'products/products.html', {
        "products": products,
    })

def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product.html', {
        "product": product
    })
