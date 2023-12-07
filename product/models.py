from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.TextChoices):
    PC = 'PC'
    PHONE = 'Phone'
    HOME = 'Home'
    CAR = 'Car'
    CLOTHES = 'Clothes'


class Product(models.Model):
    title = models.CharField(max_length=50, default="", blank=False)
    discribtion = models.TextField(max_length=500, default="", blank=False)
    brand = models.TextField(max_length=500, default="", blank=False)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=1, decimal_places=1, null=True, blank=True)
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=50, choices=Category.choices)

    def __str__(self):
        return self.title