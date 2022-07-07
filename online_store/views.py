from django.shortcuts import render
from products.models import Product, WishList

def homepage(request):
    products = Product.objects.all()[:5]
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user)
        wishlist = len(wishlist)
    else:
        wishlist = False
    return render(request, 'homepage.html', {
        "products": products,
        "wishlist":wishlist
    })