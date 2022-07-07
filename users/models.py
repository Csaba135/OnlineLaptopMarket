from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
    date_of_birth = models.DateField(max_length=8, null=True)
    age = models.IntegerField(null=True)
    nationality = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.user.email

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **kwargs)

class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), blank=False, null=False, unique=True)

    objects=UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
