# pizza/views.py
from datetime import datetime
from venv import logger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .forms import PizzaForm, OrderForm, PizzaFilterForm
from .models import Pizza, Order, PromoCode
from registration.models import Courier


def index(request):
    logger.info("Redirecting to pizza list")
    return redirect('pizza:pizza_list')


def pizza_list(request):
    logger.debug("Fetching all pizzas and promo codes")
    pizzas = Pizza.objects.all()
    promo_codes = PromoCode.objects.all()

    form = PizzaFilterForm(request.GET)
    if form.is_valid():
        logger.debug("Pizza filter form is valid")
        if form.cleaned_data['sauce_search']:
            logger.debug(f"Filtering pizzas with sauce containing: {form.cleaned_data['sauce_search']}")
            pizzas = pizzas.filter(sauce__icontains=form.cleaned_data['sauce_search'])
        if form.cleaned_data['sort_by'] == 'price_asc':
            logger.debug("Sorting pizzas by ascending price")
            pizzas = pizzas.order_by('price')
        elif form.cleaned_data['sort_by'] == 'price_desc':

            logger.debug("Sorting pizzas by descending price")
            pizzas = pizzas.order_by('-price')

    context = {
        'pizzas': pizzas,
        'promo_codes': promo_codes,
        'form': form,
    }
    logger.info("Rendering pizza list")
    return render(request, 'pizza_list.html', context)


@login_required
def pizza_detail(request, pizza_id):
    logger.debug(f"Fetching pizza with id: {pizza_id}")
    pizza = get_object_or_404(Pizza, id=pizza_id)
    logger.info("Rendering pizza detail")
    return render(request, 'pizza_detail.html', {'pizza': pizza})


@login_required
def pizza_create(request):
    if request.method == 'POST':
        logger.debug("Creating new pizza")
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("New pizza created successfully")
            return redirect('pizza:pizza_list')
    else:
        form = PizzaForm()
    return render(request, 'pizza_form.html', {'form': form})


def add_to_cart(request, pizza_id):
    logger.debug(f"Adding pizza with id {pizza_id} to the cart")
    pizza = get_object_or_404(Pizza, id=pizza_id)

    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    if str(pizza_id) in cart:
        cart[str(pizza_id)] += 1
    else:
        cart[str(pizza_id)] = 1

    request.session['cart'] = cart
    logger.info("Pizza added to the cart successfully")

    return redirect('pizza:view_cart')


@login_required
def view_cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    logger.debug("Viewing shopping cart")
    cart = request.session.get('cart', {})
    pizzas_in_cart = Pizza.objects.filter(id__in=cart.keys())

    total_price = sum(cart[str(pizza.id)] * pizza.price for pizza in pizzas_in_cart)

    return render(request, 'view_cart.html',
                  {'cart': cart, 'pizzas_in_cart': pizzas_in_cart, 'total_price': total_price})


@login_required
def remove_from_cart(request, pizza_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    logger.debug(f"Removing pizza with id {pizza_id} from the cart")

    if 'cart' in request.session:
        cart = request.session['cart']

        if str(pizza_id) in cart:
            if cart[str(pizza_id)] > 1:
                cart[str(pizza_id)] -= 1
            else:
                del cart[str(pizza_id)]

        request.session['cart'] = cart
        logger.info("Pizza removed from the cart successfully")

    return redirect('pizza:view_cart')


@login_required
def clear_cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    logger.debug("Clearing the shopping cart")

    if 'cart' in request.session:
        del request.session['cart']

    logger.info("Cart cleared successfully")

    return redirect('pizza:view_cart')


@login_required
def order_pizza(request, pizza_id):
    logger.debug(f"Ordering pizza with id: {pizza_id}")
    pizza = get_object_or_404(Pizza, id=pizza_id)
    quantity = 1  # Assume a default quantity for simplicity, you might want to modify this
    total_price = quantity * pizza.price
    order = Order.objects.create(client=request.user, pizza=pizza, quantity=quantity, total_price=total_price)
    logger.info("Pizza ordered successfully")
    return render(request, 'order_confirmation.html', {'order': order, 'pizza': pizza})


@login_required
def confirm_order(request):
    logger.debug("Confirming order")

    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    promo_code = request.POST.get('promo_code')
    orders = []
    for pizza_id in cart.keys():
        pizza = get_object_or_404(Pizza, id=pizza_id)
        order = Order.objects.create(client=request.user, pizza=pizza, quantity=cart[str(pizza_id)],
                                     total_price=pizza.price * cart[str(pizza_id)])
        order.save()
        orders.append(order)
    cart = {}
    request.session['cart'] = cart
    if promo_code:
        try:
            promo = get_object_or_404(PromoCode, code=promo_code, is_active=True)
            for order in orders:
                order.discount = promo.discount
                order.save()
        except PromoCode.DoesNotExist:
            error_message = "Invalid or inactive promo code"
            return render(request, 'order_confirmation.html', {'order': order, 'error_message': error_message})
    return redirect(to='pizza:payment')

@login_required
def payment_view(request):
    return render(request, 'payment.html')

@login_required
def pizza_edit(request, pizza_id):
    logger.debug(f"Editing pizza with id: {pizza_id}")
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            logger.info(f"Pizza with id {pizza_id} updated successfully")
            return redirect('pizza:pizza_detail', pizza_id=pizza.id)
        else:
            logger.warning("Pizza form is invalid")
    else:
        form = PizzaForm(instance=pizza)
    return render(request, 'pizza_form.html', {'form': form})


@login_required
def order_create(request):
    if request.method == 'POST':
        logger.debug("Creating new order")
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = request.user
            order.total_price = order.pizza.price * order.quantity
            order.save()
            logger.info("New order created successfully")
            return redirect('pizza:order_list')
        else:
            logger.warning("Order form is invalid")
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})


def staff_required(user):
    return user.is_staff


@user_passes_test(staff_required)
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    logger.info("Rendering pizza detail")
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
    order.courier = request.user
    courier = get_object_or_404(Courier, user=order.courier)
    courier.total_deliveries += 1
    courier.save()
    order.save()
    return redirect('pizza:order_list')
