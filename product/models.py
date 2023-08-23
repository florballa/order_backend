from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    default_price = models.FloatField(max_length=10)
    description = models.CharField(max_length=50)
    categories = models.ManyToManyField(ProductCategory, related_name='products')

    def __str__(self):
        return self.name
