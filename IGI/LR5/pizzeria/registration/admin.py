# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Courier, Customer


class CourierInline(admin.StackedInline):
    model = Courier
    can_delete = False
    verbose_name_plural = 'courier'


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customer'


class UserAdmin(BaseUserAdmin):
    inlines = (CourierInline, CustomerInline)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if hasattr(obj, 'courier_profile'):
            obj.is_staff = True
            obj.save()


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone_number', 'total_orders', 'total_spent')
    search_fields = ('user__username', 'telephone_number')

    def total_orders(self, obj):
        return obj.total_orders()

    def total_spent(self, obj):
        return obj.total_spent()

    total_orders.short_description = 'Total Orders'
    total_spent.short_description = 'Total Spent'


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_earnings')
    search_fields = ('user__username',)

    def total_earnings(self, obj):
        return obj.total_earnings()

    total_earnings.short_description = 'Total Earnings'
