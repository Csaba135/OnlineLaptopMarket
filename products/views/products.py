from products.models import Product, WishList
from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse
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
        wishlist_form = WishListForm(user=user, product=product)
    else:
        form1 = NotificationForm(request.POST, product=product)
        try:
            wishlist_form = WishListForm(request.POST, user=user, product=product)
        except:
            pass
        if form1.is_valid():
            form1.save()
            return redirect(reverse('products:all_products'))
        try:
            if wishlist_form.is_valid():
                wishlist_form.save()
            return redirect(reverse('products:wishlist'))
        except:
            pass
    return render(request, 'products/product.html', {
        'product': product,
        'form1':form1,
        'wishlist_form':wishlist_form,
        'w': w,
        'wishlisted':wishlisted,
    })
    # try:
    #     l = Like.objects.filter(product=product).filter(user=user)
    #     if l.exists():
    #         l = False
    #     else:
    #         l = True
    # except:
    #     l = False
    # try:
    #     d = Dislike.objects.filter(product=product).filter(user=user)
    #     if d.exists():
    #         d = False
    #     else:
    #         d = True
    # except:
    #     d = False

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