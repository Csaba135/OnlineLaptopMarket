from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(max_length=8)
    age = models.IntegerField()
    nationality = models.CharField(max_length=128)
