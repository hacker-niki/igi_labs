from datetime import date, datetime

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from pizza.models import Order, Pizza

from .models import Customer, Courier


class CustomerCourierTests(TestCase):

    def setUp(self):
        # Create a user
        self.user1 = User.objects.create_user(username='customer1', password='password')
        self.user2 = User.objects.create_user(username='courier1', password='password')

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
        Order.objects.create(client=self.user1, pizza=self.pizza, quantity=2)
        Order.objects.create(client=self.user1, pizza=self.pizza, quantity=1)

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


class RegistrationViewTests(TestCase):

    def setUp(self):
        # Initialize the test client
        self.client = Client()

        # Create a pizza and user for testing
        self.pizza = Pizza.objects.create(price=10)
        self.user1 = User.objects.create_user(username='customer1', password='password')
        self.customer = Customer.objects.create(
            user=self.user1,
            date_of_birth=date(1990, 1, 1),
            telephone_number='+1234567890'
        )

    def test_user_profile_view(self):
        self.client.login(username='customer1', password='password')
        response = self.client.get(reverse('registration:user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')
        self.assertEqual(response.context['customer'], self.customer)
        self.assertEqual(response.context['user_timezone'], 'UTC')
        self.assertIsInstance(response.context['current_date_user_tz'], datetime)
        self.assertIsInstance(response.context['current_date_utc'], datetime)

    def test_user_profile_view_with_timezone(self):
        self.client.login(username='customer1', password='password')
        response = self.client.post(reverse('registration:user_profile'), {'timezone': 'Asia/Kolkata'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')
        self.assertEqual(response.context['user_timezone'], 'Asia/Kolkata')
        self.assertIsInstance(response.context['current_date_user_tz'], datetime)
        self.assertIsInstance(response.context['current_date_utc'], datetime)
