from django.urls import path

from . import views

app_name = 'pizza'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('pizza_list/', views.pizza_list, name='pizza_list'),
    path('client_orders_count/', views.client_orders_count, name='client_orders_count'),
    path('courier_total_sales/', views.courier_total_sales, name='courier_total_sales'),
    path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('pizza/edit/<int:pizza_id>/', views.pizza_edit, name='pizza_edit'),
    path('order/<int:pizza_id>/', views.order_pizza, name='order_pizza'),
]
