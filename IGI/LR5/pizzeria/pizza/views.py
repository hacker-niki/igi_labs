# pizza/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Sum
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
    # Implement your order logic here (e.g., create an Order object)
    # For now, let's redirect to a dummy confirmation page
    return render(request, 'order_confirmation.html', {'pizza': pizza})


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
def order_list(request):
    if request.user.is_staff:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(client=request.user)
    return render(request, 'order_list.html', {'orders': orders})


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
def client_orders_count(request):
    if request.user.is_staff:
        clients_orders = User.objects.annotate(order_count=Count('order')).filter(order_count__gt=0)
    else:
        clients_orders = None
    return render(request, 'client_orders_count.html', {'clients_orders': clients_orders})


@login_required
def courier_total_sales(request):
    if request.user.is_staff:
        couriers_sales = User.objects.annotate(total_sales=Sum('deliveries__total_price')).filter(total_sales__gt=0)
    else:
        couriers_sales = None
    return render(request, 'courier_total_sales.html', {'couriers_sales': couriers_sales})


@login_required
def promo_code_list(request):
    promo_codes = PromoCode.objects.filter(is_active=True)
    return render(request, 'promo_code_list.html', {'promo_codes': promo_codes})


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
