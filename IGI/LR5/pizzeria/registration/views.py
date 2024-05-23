from datetime import datetime

import pytz
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from pizza.models import Order
from registration.models import Customer

from .forms import CustomUserCreationForm


# Create your views here.
def create_account(request):
    form = CustomUserCreationForm

    # If the HTTP method is POST we check the form for validity
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)

        # If the form is valid, save the form and preform a redirect
        if form.is_valid():
            form.save()

            # Create a message telling the user a new account was created
            account_name = form.cleaned_data['username']
            messages.success(
                request,
                f'A new account named {account_name} has been created!'
            )

            return redirect('registration:login')

    return render(request, 'create_account.html', {'form': form})


def login_user(request):
    form = AuthenticationForm

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Get the user and log them in
            user = form.get_user()
            login(request, user)

            return redirect('pizza:homepage')

    return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('pizza:homepage')


@login_required
def user_profile(request):
    user = request.user
    try:
        customer = Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        return redirect('create_account')

    orders = Order.objects.filter(client=user).order_by('-created_at')

    # Get user's timezone from the request (default to UTC if not provided)
    user_timezone_str = request.POST.get('timezone', 'UTC')
    try:
        user_timezone = pytz.timezone(user_timezone_str)
    except pytz.UnknownTimeZoneError:
        user_timezone = pytz.UTC

    # Current date in user's timezone and UTC
    current_date_user_tz = datetime.now(user_timezone)
    current_date_utc = datetime.utcnow().replace(tzinfo=pytz.utc)

    return render(request, 'user_profile.html', {
        'customer': customer,
        'orders': orders,
        'user_timezone': user_timezone_str,
        'current_date_user_tz': current_date_user_tz,
        'current_date_utc': current_date_utc
    })
