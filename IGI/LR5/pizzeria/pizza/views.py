# pizza/views.py
from datetime import timezone, datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .forms import PizzaForm, OrderForm, PromoCodeForm, PizzaFilterForm
from .models import Pizza, Order, PromoCode


def index(request):
    return redirect('pizza:pizza_list')


def pizza_list(request):
    pizzas = Pizza.objects.all()
    promo_codes = PromoCode.objects.all()

    form = PizzaFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['sauce_search']:
            pizzas = pizzas.filter(sauce__icontains=form.cleaned_data['sauce_search'])
        if form.cleaned_data['sort_by'] == 'price_asc':
            pizzas = pizzas.order_by('price')
        elif form.cleaned_data['sort_by'] == 'price_desc':
            pizzas = pizzas.order_by('-price')

    context = {
        'pizzas': pizzas,
        'promo_codes': promo_codes,
        'form': form,
    }
    return render(request, 'pizza_list.html', context)


@login_required
def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'pizza_detail.html', {'pizza': pizza})


@login_required
def pizza_create(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza:pizza_list')
    else:
        form = PizzaForm()
    return render(request, 'pizza_form.html', {'form': form})


@login_required
def order_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    quantity = 1  # Assume a default quantity for simplicity, you might want to modify this
    total_price = quantity * pizza.price
    order = Order.objects.create(client=request.user, pizza=pizza, quantity=quantity, total_price=total_price)
    return render(request, 'order_confirmation.html', {'order': order})


@login_required
def pizza_edit(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('pizza:pizza_detail', pizza_id=pizza.id)
    else:
        form = PizzaForm(instance=pizza)
    return render(request, 'pizza_form.html', {'form': form})


@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = request.user
            order.total_price = order.pizza.price * order.quantity
            order.save()
            return redirect('pizza:order_list')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})


@login_required
def promo_code_create(request):
    if request.method == 'POST':
        form = PromoCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza:promo_code_list')
    else:
        form = PromoCodeForm()
    return render(request, 'promo_code_form.html', {'form': form})


@login_required
def pizza_search(request):
    sauce = request.GET.get('sauce')
    if sauce:
        pizzas = Pizza.objects


def staff_required(user):
    return user.is_staff


@user_passes_test(staff_required)
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})


@user_passes_test(staff_required)
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})


@user_passes_test(staff_required)
def finish_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = True
    order.updated_at = datetime.now()
    order.save()
    return redirect('pizza:order_list')
