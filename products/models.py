from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=256)
    description = models.TextField()
    active = models.BooleanField(default=True)
