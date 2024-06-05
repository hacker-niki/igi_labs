import base64
import io
import matplotlib.pyplot as plt
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.db.models import Sum

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
    change_list_template = "admin/customers_change_list.html"

    def total_orders(self, obj):
        return obj.total_orders()

    def total_spent(self, obj):
        return obj.total_spent()

    total_orders.short_description = 'Total Orders'
    total_spent.short_description = 'Total Spent'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        # Get the total spent data
        queryset = self.get_queryset(request)
        customer_data = queryset.annotate(total_spent=Sum('user__client_orders__total_price'))
        customers = [customer.user.username for customer in customer_data]
        total_spent = [customer.total_spent or 0 for customer in customer_data]

        # Create the pie chart
        fig, ax = plt.subplots()
        ax.pie(total_spent, labels=customers, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Total Spent by Customers')

        # Save the plot to a BytesIO object
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        plt.close(fig)
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Encode the PNG image to base64 string
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')

        extra_context = extra_context or {}
        extra_context['pie_chart'] = graphic

        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_deliveries', 'total_earnings')
    search_fields = ('user__username',)

    def total_earnings(self, obj):
        return obj.total_earnings()

    total_earnings.short_description = 'Total Earnings'
