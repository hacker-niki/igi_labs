from django.urls import path

from . import views
from .views import order_list, order_detail

app_name = 'pizza'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('pizza_list/', views.pizza_list, name='pizza_list'),
    path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('pizza/edit/<int:pizza_id>/', views.pizza_edit, name='pizza_edit'),
    path('order/<int:pizza_id>/', views.order_pizza, name='order_pizza'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/finish/', views.finish_order, name='finish_order'),
]
