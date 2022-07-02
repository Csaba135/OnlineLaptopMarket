import os
import json
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction, models
from products.models import Product, Store, WishList, NotificationAboutProduct
from django.contrib.auth.models import User
from .send_mail_extension import SendMailCheaper, SendMailExpensive, SendMailSamePrice
from .helpers_extension import CreateJsonList, CreateDBList, GetMagasineID

class Command(BaseCommand):
    help = 'Import products from web scrapped application.'

    def handle(self, *args, **options):

        magasines_with_products=CreateJsonList('all products')
        products_in_json=CreateJsonList('json_products')
        products_in_db=CreateDBList()

        for product_difference in products_in_db:
            if product_difference not in products_in_json:
                Product.objects.filter(title=product_difference).delete()

        with transaction.atomic():
            for product in magasines_with_products:
                specs = product['specs']
                try:
                    normal_price_if_exist = specs['normal_price']
                except:
                    normal_price_if_exist = 0
                try:
                    store = Store.objects.get(name=product['magasine'])
                except Store.DoesNotExist:
                    store = Store(name=product['magasine'])
                    store.save()
                magasine_id = GetMagasineID(product["magasine"])
                if Product.objects.filter(title=specs['title']).filter(store_id=magasine_id).exists():
                    for product_title in products_in_db:
                        if specs['title'] == product_title:
                            store=Store.objects.get(id=magasine_id)
                            product=Product.objects.filter(title=specs['title']).filter(store_id=magasine_id)
                            for p in product:
                                if float(p.price_to_compare) > float(specs['price']):
                                    # mai trebuie sa iau datele din wishlist
                                   # SendMailCheaper(specs['price'], specs['title'])
                                elif float(p.price_to_compare) < float(specs['price']):
                                    # mai trebuie sa iau datele din wishlist
                                    #SendMailExpensive(specs['price'], specs['title'])
                                else:
                                    # mai trebuie sa iau datele din wishlist
                                    #SendMailSamePrice(specs['price'], specs['title'])
                            my_object = Product.objects.get(id=p.product_id)
                            my_object.price = specs['price']
                            my_object.normal_price = normal_price_if_exist
                            my_object.link = specs['link']
                            my_object.image = f'products/{specs["id"]}.jpg'
                            my_object.save()
                else:
                    Product.objects.create(
                        store=store,
                        title = specs['title'],
                        price = specs['price'],
                        normal_price=normal_price_if_exist,
                        processor_type = specs['processor_type'],
                        memory_type = specs['memory_type'],
                        RAM = specs['RAM'],
                        GPU = specs['GPU'],
                        screen_resolution = specs['screen_resolution'],
                        link = specs['link'],
                        image=f'products/{specs["id"]}.jpg',
                    )