from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, Store
from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator


def get_all_products(request):
    products = Product.objects.order_by('price').all()

    paginator = Paginator(products, 20)

    page = request.GET.get('page', 1)
    products_page = paginator.get_page(page)

    return render(request, 'products/products.html', {
        "products": products,
        "products_page": products_page,
    })



def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product.html', {
        "product": product,
    })
