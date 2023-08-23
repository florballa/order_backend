from django.contrib.auth.models import User
from django.db import models

from agent.models import Costumer
from product.models import Product


class Counter(models.Model):
    name = models.CharField(max_length=10)
    value = models.IntegerField()


class Order(models.Model):
    code = models.IntegerField()
    code_year = models.CharField(max_length=10)
    date_registered = models.DateField(auto_now_add=True)
    costumer = models.ForeignKey(Costumer, related_name='orders', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class OrderUnit(models.Model):
    order = models.ForeignKey(Order, related_name='order_units', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_units', on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.amount
