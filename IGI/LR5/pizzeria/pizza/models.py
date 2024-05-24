from django.contrib.auth.models import User
from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    sauce = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/pizza/')

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_orders')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='courier_orders', null=True,
                                blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    status = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.id} by {self.client.username}"

    def save(self, *args, **kwargs):
        self.total_price = float(self.quantity) * float(self.pizza.price) * (1 - float(self.discount))
        super().save(*args, **kwargs)


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
