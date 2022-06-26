import os
import json
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from products.models import Product, Store


class Command(BaseCommand):
    help = 'Import products from web scrapped application.'

    def handle(self, *args, **options):
        print('Here is my first Django command.')

        with open(os.path.join('products\web_scrapers','output.json')) as json_file:
            magasine_with_products = json.load(json_file)

        with transaction.atomic():
            for product in magasine_with_products:
                specs = product['specs']
                def get_number_from_string():
                    return specs['price'].split(' ')[0]

                def get_price_from_string():
                    return float(get_number_from_string().replace('.', '').replace(',', '.'))

                try:
                    def get_normal_number_from_string():
                        return specs['normal_price'].split(' ')[0]
                    def get_normal_price_from_string():
                        try:
                            return float(get_normal_number_from_string().replace('.', '').replace(',', '.'))
                        except:
                            return 0
                except:
                    pass

                try:
                    store = Store.objects.get(name=product['magasine'])
                except Store.DoesNotExist:
                    store = Store(name=product['magasine'])
                    store.save()
                try:
                    Product.objects.get(title=specs['title'])
                except Product.DoesNotExist:
                    Product.objects.create(
                        store=store,
                        title = specs['title'],
                        price = get_price_from_string(),
                        normal_price = get_normal_price_from_string(),
                        processor_type = specs['processor_type'],
                        memory_type = specs['memory_type'],
                        RAM = specs['RAM'],
                        GPU = specs['GPU'],
                        screen_resolution = specs['screen_resolution'],
                        link = specs['link'],
                        image=f'products/{specs["id"]}.jpg',
                    )
