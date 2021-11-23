from django.db import models
from django.contrib.auth import get_user_model

from catalogue.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} ({self.quantity})'


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_quantity(self):
        return sum([item.quantity for item in self.items.all()])

    def get_total_price(self):
        return sum([item.product.price * item.quantity for item in self.items.all()])

    def __str__(self):
        return f'{self.get_total_quantity()} items for {self.get_total_price()} € ({self.user.username})'
