from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    date_of_birth = models.DateField(blank=True, null=True)
    telephone_number = PhoneNumberField()

    def total_orders(self):
        return self.user.client_orders.count()

    def total_spent(self):
        return self.user.client_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

    def __str__(self):
        return f"Customer {self.user.username}"


class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='courier_profile')
    total_deliveries = models.IntegerField(default=0)

    def total_earnings(self):
        return self.user.courier_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

    def __str__(self):
        return f"Courier {self.user.username}"
