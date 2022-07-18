from django.core.management.base import BaseCommand
from django.db import transaction
from products.models import Product, Store
from .send_mail_extension import send_mail_expensive,send_mail_same_price,send_mail_cheaper
from .helpers_extension import create_DB_list, create_json_list, get_email_list, get_magasineID

class Command(BaseCommand):
    help = 'Import products from web scrapped application.'

    def handle(self, *args, **options):

        magasines_with_products=create_json_list('all products')
        products_in_json=create_json_list('json_products')
        products_in_db=create_DB_list()

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
                magasine_id = get_magasineID(product["magasine"])
                if Product.objects.filter(title=specs['title']).filter(store_id=magasine_id).exists():
                    for product_title in products_in_db:
                        if specs['title'] == product_title:
                            product=Product.objects.filter(title=specs['title']).filter(store_id=magasine_id)
                            for p in product:
                                if float(p.price_to_compare) > float(specs['price']):
                                    email_list = list(get_email_list(p.product_id))
                                    if email_list:
                                        send_mail_cheaper(specs['price'], specs['title'],  email_list)
                                elif float(p.price_to_compare) < float(specs['price']):
                                    email_list = list(get_email_list(p.product_id))
                                    if email_list:
                                        send_mail_expensive(specs['price'], specs['title'], email_list)
                                else:
                                    email_list = list(get_email_list(p.product_id))
                                    if email_list:
                                        send_mail_same_price(specs['price'], specs['title'], email_list)
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