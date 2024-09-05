from django.urls import path

from . import views
from .views import order_list

app_name = 'pizza'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('pizza_list/', views.pizza_list, name='pizza_list'),
    path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('pizza/edit/<int:pizza_id>/', views.pizza_edit, name='pizza_edit'),
    path('order/<int:pizza_id>/', views.add_to_cart, name='order_pizza'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('cart/', views.view_cart, name='view_cart'),
    path('payment/', views.payment_view, name='payment'),
    path('remove_from_cart/<int:pizza_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/finish/', views.finish_order, name='finish_order'),
]
