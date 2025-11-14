from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    snils = models.CharField(max_length=11)
    post = models.CharField(max_length=254)
    organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.SET_NULL, related_name='users')
    is_hr = models.BooleanField(default=False)



class Organization(models.Model):
    name = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254)
    name_prepositional = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254)
    email = models.EmailField(max_length=100)
    inn = models.CharField(max_length=10, unique=True)
    ogrn = models.CharField(max_length=13, unique=True)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.inn}'

