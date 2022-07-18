from django import forms
from products.models import NotificationAboutProduct, WishList, Product, Store


class NotificationForm(forms.ModelForm):
    class Meta:
        model = NotificationAboutProduct
        exclude = ['product']

    def __init__(self, *args, **kwargs):
        self._product = kwargs.pop('product')

        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        notify = super().save(commit=False)
        notify.product = self._product

        if commit is True:
            notify.save()

        return notify

class WishListForm(forms.ModelForm):
    class Meta:
        model = WishList
        exclude = ['product', 'user']

    def __init__(self, *args, **kwargs):
        self._product = kwargs.pop('product')
        self._user = kwargs.pop('user')

        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        wishlist = super().save(commit=False)
        wishlist.product = self._product
        wishlist.user = self._user

        if commit is True:
            wishlist.save()

        return wishlist


class FilterForm(forms.Form):
    order_by_choices = (
        ('price_asc', 'Price ascending'),
        ('price_desc', 'Price descending'),
        ('title', 'Title'),
        ('title_reverse', 'Title Reverse'),
        ('store', 'Store'),
        ('screen', 'Screen'),
    )
    stores = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False, choices=(
        (store.id, store.name)
        for store in Store.objects.all()
    ))
    title = forms.CharField(max_length=255, required=False)
    price_min = forms.IntegerField(min_value=0, required=False)
    price_max = forms.IntegerField(min_value=0, required=False)
    order_by = forms.ChoiceField(widget=forms.Select, choices=order_by_choices, required=False)

    def get_results(self):
        title = self.cleaned_data.get('title')
        price_min = self.cleaned_data.get('price_min')
        price_max = self.cleaned_data.get('price_max')
        order_by = self.cleaned_data.get('order_by')
        store_ids = self.cleaned_data.get('stores')

        if order_by == 'price_asc':
            products = Product.objects.order_by('price')
        elif order_by == 'price_desc':
            products = Product.objects.order_by('-price')
        elif order_by == 'title':
            products = Product.objects.order_by('title')
        elif order_by == 'title_reverse':
            products = Product.objects.order_by('-title')
        elif order_by == 'store':
            products = Product.objects.order_by('store')
        else:
            products = Product.objects.order_by('-screen_resolution')

        if title:
            products = products.filter(title__icontains=title)

        if price_min:
            products = products.filter(price__gte=price_min)

        if price_max:
            products = products.filter(price__lte=price_max)

        if len(store_ids) > 0:
            products = products.filter(store__id__in=store_ids)

        return products.all()