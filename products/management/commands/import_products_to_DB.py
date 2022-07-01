import os
import json
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction, models
from products.models import Product, Store, WishList, NotificationAboutProduct
from django.contrib.auth.models import User
from .send_mail_extension import SendMailCheaper, SendMailExpensive, SendMailSamePrice


class Command(BaseCommand):
    help = 'Import products from web scrapped application.'

    def handle(self, *args, **options):

        with open(os.path.join('output.json')) as json_file:
            magasines_with_products = json.load(json_file)

        SendMailCheaper(225, 'Marha')

        products_in_db=[]
        products_existing_in_db = Product.objects.all()
        for product in products_existing_in_db:
            products_in_db.append(product.title_to_compare)

        products_in_json = []
        for product in  magasines_with_products:
            specs = product['specs']
            products_in_json.append(specs['title'])

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
                if specs['title'] in products_in_db:
                    for product_title in products_in_db:
                        if specs['title'] == product_title:
                            price = Product.objects.filter(price=specs['price']).filter(title=product_title)
                            store = Store.objects.filter(name=product['magasine'])
                            for p, s in zip(price, store):
                                if s.store_id_s == p.store_id_p:
                                    if float(p.price_to_compare) > float(specs['price']):
                                        # mai trebuie sa iau datele din wishlist
                                        SendMailCheaper(specs['price'], specs['title'])
                                        print("price is smaler")
                                    elif float(p.price_to_compare) < float(specs['price']):
                                        # mai trebuie sa iau datele din wishlist
                                        SendMailExpensive(specs['price'], specs['title'])
                                        print("price is bigger")
                                    else:
                                        # mai trebuie sa iau datele din wishlist
                                        SendMailSamePrice(specs['price'], specs['title'])
                                        print("price is the same")
                else:
                    print("Not in there")
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