from django.shortcuts import render
from products.models import Product

def homepage(request):
    products = Product.objects.all()[:5]

    return render(request, 'homepage.html', {
        "products": products,
    })