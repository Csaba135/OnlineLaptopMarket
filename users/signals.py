from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from users.models import Customer

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_customer(instance, **kwargs):
    if not hasattr(instance, 'customer'):
        Customer.objects.create(user=instance)