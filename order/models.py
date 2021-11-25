from typing import DefaultDict
from django.db import models
from django.conf import settings
from shop.models import Product



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user} - {self.id}'

    def get_total_price(self):
        return sum(item.get_const() for item in self.items.all())



class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)


    def __str__(self):
        return f'{self.id}'


    def get_const(self):
        return self.price * self.quantity