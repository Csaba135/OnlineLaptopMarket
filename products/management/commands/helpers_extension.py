import os
import json
from products.models import Product, Store, WishList, NotificationAboutProduct



def CreateJsonList(param1):

    with open(os.path.join('output.json')) as json_file:
        magasines_with_products = json.load(json_file)

    products_in_json = []
    for product in magasines_with_products:
        specs = product['specs']
        products_in_json.append(specs['title'])
    if param1=='all products':
        return magasines_with_products
    else:
        return products_in_json
def CreateDBList():
    products_in_db = []
    products_existing_in_db = Product.objects.all()
    for product in products_existing_in_db:
        products_in_db.append(product.title_to_compare)

    return products_in_db

def GetMagasineID(param1):

    stores=Store.objects.all()
    for store in stores:
        if param1 == store.name_to_compare:
            return int(store.store_id_s)

def GetEmailList(product_id):
    wishlist=WishList.objects.filter(product=product_id)
    notify=NotificationAboutProduct.objects.filter(product=product_id)
    email_set=set()
    for w in wishlist:
        email_set.add(w.user.email)
    for n in notify:
        email_set.add(n.email)
    return email_set