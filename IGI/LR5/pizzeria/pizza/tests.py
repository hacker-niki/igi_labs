import os
from datetime import date
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from pizza.models import Order, Pizza, PromoCode
from registration.models import Customer, Courier

from .models import Pizza, Order, PromoCode

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')


class PizzaModelTests(TestCase):
    def setUp(self):
        self.pizza = Pizza.objects.create(
            name='Test Pizza',
            sauce='Tomato',
            price=Decimal('10.00'),
            image='media/pizza/test_pizza.jpg'
        )

    def test_pizza_creation(self):
        self.assertEqual(self.pizza.name, 'Test Pizza')
        self.assertEqual(self.pizza.sauce, 'Tomato')
        self.assertEqual(self.pizza.price, Decimal('10.00'))
        self.assertEqual(self.pizza.image, 'media/pizza/test_pizza.jpg')

    def test_pizza_str(self):
        self.assertEqual(str(self.pizza), 'Test Pizza')


class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.courier = User.objects.create_user(username='courieruser', password='12345')
        self.pizza = Pizza.objects.create(
            name='Test Pizza',
            sauce='Tomato',
            price=Decimal('10.00'),
            image='media/pizza/test_pizza.jpg'
        )
        self.order = Order.objects.create(
            client=self.user,
            pizza=self.pizza,
            quantity=2,
            total_price=Decimal('20.00'),
            courier=self.courier
        )

    def test_order_creation(self):
        self.assertEqual(self.order.client, self.user)
        self.assertEqual(self.order.pizza, self.pizza)
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.total_price, Decimal('20.00'))
        self.assertEqual(self.order.courier, self.courier)
        self.assertFalse(self.order.status)

    def test_order_str(self):
        self.assertEqual(str(self.order), f"Order {self.order.id} by {self.user.username}")

    def test_order_total_price_calculation(self):
        self.order.quantity = 3
        self.order.save()
        self.assertEqual(self.order.total_price, Decimal('30.00'))


class PromoCodeModelTests(TestCase):
    def setUp(self):
        self.promo_code = PromoCode.objects.create(
            code='DISCOUNT10',
            discount=Decimal('10.00')
        )

    def test_promo_code_creation(self):
        self.assertEqual(self.promo_code.code, 'DISCOUNT10')
        self.assertEqual(self.promo_code.discount, Decimal('10.00'))
        self.assertTrue(self.promo_code.is_active)

    def test_promo_code_str(self):
        self.assertEqual(str(self.promo_code), 'DISCOUNT10')


class CustomerCourierTests(TestCase):

    def setUp(self):
        # Create a user
        self.user1 = User.objects.create_user(username='customer1', password='password')
        self.user2 = User.objects.create_user(username='courier1', password='password', is_staff=True)

        # Create a customer profile
        self.customer = Customer.objects.create(
            user=self.user1,
            date_of_birth=date(1990, 1, 1),
            telephone_number='+1234567890'
        )
        self.pizza = Pizza.objects.create(price=10)

        # Create a courier profile
        self.courier = Courier.objects.create(
            user=self.user2,
            total_deliveries=5
        )

        # Create orders for the customer
        Order.objects.create(client=self.user1, pizza=self.pizza, quantity=2, total_price=20)
        Order.objects.create(client=self.user1, pizza=self.pizza, quantity=1, total_price=10)

    def test_customer_total_orders(self):
        self.assertEqual(self.customer.total_orders(), 2)

    def test_customer_total_spent(self):
        self.assertEqual(self.customer.total_spent(), 30)

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'Customer customer1')

    def test_courier_total_earnings(self):
        self.assertEqual(self.courier.total_earnings(), 0)

    def test_courier_str(self):
        self.assertEqual(str(self.courier), 'Courier courier1')

    def test_courier_total_deliveries(self):
        self.assertEqual(self.courier.total_deliveries, 5)


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='customer1', password='password')
        self.user2 = User.objects.create_user(username='courier1', password='password', is_staff=True)

        self.customer = Customer.objects.create(
            user=self.user1,
            date_of_birth=date(1990, 1, 1),
            telephone_number='+1234567890'
        )
        self.pizza = Pizza.objects.create(price=10)
        self.courier = Courier.objects.create(user=self.user2, total_deliveries=5)
        Order.objects.create(client=self.user1, pizza=self.pizza, quantity=2, total_price=20)
        Order.objects.create(client=self.user1, pizza=self.pizza, quantity=1, total_price=10)

    def test_order_pizza_view(self):
        self.client.login(username='customer1', password='password')
        response = self.client.post(reverse('pizza:order_pizza', args=[self.pizza.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_confirmation.html')

    def test_order_detail_view(self):
        self.client.login(username='courier1', password='password')
        order = Order.objects.first()
        response = self.client.get(reverse('pizza:order_detail', args=[order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_detail.html')

    def test_finish_order_view(self):
        self.client.login(username='courier1', password='password')
        order = Order.objects.first()
        response = self.client.post(reverse('pizza:finish_order', args=[order.id]))
        self.assertRedirects(response, reverse('pizza:order_list'))
        order.refresh_from_db()
        self.assertTrue(order.status)
