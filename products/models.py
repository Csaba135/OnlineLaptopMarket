from django.db import models
from users.models import Customer

class Store(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    logo = models.ImageField(upload_to='stores/', null=True, default=None)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    normal_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    processor_type = models.CharField(max_length=128)
    memory_type = models.CharField(max_length=128)
    RAM = models.CharField(max_length=128)
    GPU = models.CharField(max_length=128)
    screen_resolution = models.CharField(max_length=128)
    link = models.URLField()
    image = models.ImageField(upload_to='products/', null=True, default=None)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

class NotificationAboutProduct(models.Model):
    email = models.EmailField(('email address'), blank=False, null=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)