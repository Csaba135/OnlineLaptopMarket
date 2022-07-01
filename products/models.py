from django.db import models
from users.models import Customer

class Store(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    logo = models.ImageField(upload_to='stores/', null=True, default=None)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def store_id_s(self):
        return self.id

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,unique=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    normal_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    processor_type = models.CharField(max_length=128)
    memory_type = models.CharField(max_length=128)
    RAM = models.CharField(max_length=128)
    GPU = models.CharField(max_length=128)
    screen_resolution = models.CharField(max_length=128, default="1920 x 1080")
    link = models.URLField(max_length=1000)
    image = models.ImageField(upload_to='products/', null=True, default=None)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    @property
    def image_url(self):
            return self.image.url

    @property
    def price_to_compare(self):
        return self.price

    @property
    def  store_id_p(self):
        return self.store_id

    @property
    def title_to_compare(self):
        return self.title

    @property
    def product_id(self):
        return self.id

    def __str__(self):
        return self.title



class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.name

class NotificationAboutProduct(models.Model):
    email = models.EmailField(('email address'), blank=False, null=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.email