from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    img = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
