from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, Store, WishList, NotificationAboutProduct
from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.core.paginator import Paginator
from products.forms import NotificationForm, WishListForm, FilterForm


def get_all_products(request):
    filter_form = FilterForm(request.GET)
    if filter_form.is_valid():
        products = filter_form.get_results()
    else:
        raise Http404('Search and filter form is invalid!')

    paginator = Paginator(products, 20)

    page = request.GET.get('page', 1)
    products_page = paginator.get_page(page)


    return render(request, 'products/products.html', {
        "products": products,
        "products_page": products_page,
        "form":filter_form,
        "total_products": len(products)

    })



def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    wishlisted = WishList.objects.filter(product=product)
    wishlisted=len(wishlisted)
    try:
        w = WishList.objects.filter(product=product).filter(user=user)
        if w.exists():
            w = False
        else:
            w = True
    except:
        w = False
    if request.method == 'GET':
        form1 = NotificationForm(product=product)
        form2 = WishListForm(user=user, product=product)
    else:
        form1 = NotificationForm(request.POST, product=product)
        try:
            form2 = WishListForm(request.POST, user=user, product=product)
        except:
            pass
        if form1.is_valid():
            form1.save()
        try:
            if form2.is_valid():
                form2.save()
            return redirect(reverse('products:wishlist'))
        except:
            pass
    return render(request, 'products/product.html', {
        'product': product,
        'form1':form1,
        'form2':form2,
        'w': w,
        'wishlisted':wishlisted
    })

def wishlist(request):
    user=request.user
    wishlist=WishList.objects.filter(user=user)
    return render(request, 'products/wishlist.html', {
        'wishlist':wishlist
    })

def delete_from_wishlist(request, product_id):
    product = get_object_or_404(WishList, user=request.user, product=product_id)
    product.delete()
    return redirect(reverse('products:wishlist'))