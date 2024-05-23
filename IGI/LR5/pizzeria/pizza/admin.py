from django.contrib import admin

from .models import Pizza, Order, PromoCode


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'sauce', 'price')
    search_fields = ('name', 'sauce')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'pizza', 'quantity', 'total_price', 'courier', 'created_at', 'updated_at', 'status')
    search_fields = ('client__username', 'courier__username', 'pizza__name')
    list_filter = ('status', 'created_at')


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'is_active')
    search_fields = ('code',)
    list_filter = ('is_active',)
