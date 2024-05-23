# pizza/forms.py

from django import forms
from django.contrib.auth.models import User

from .models import Pizza, Order, PromoCode


class PizzaFilterForm(forms.Form):
    SORT_CHOICES = [
        ('price_asc', 'Цена по возрастанию'),
        ('price_desc', 'Цена по убыванию'),
    ]
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False)
    sauce_search = forms.CharField(max_length=100, required=False, label='Поиск по соусу', initial="")


class PizzaForm(forms.ModelForm):
    price = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))

    class Meta:
        model = Pizza
        fields = ['name', 'sauce', 'price']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizza', 'quantity', 'courier']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courier'].required = False


class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code', 'discount', 'is_active']


class OrderUpdateForm(forms.ModelForm):
    courier = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True), required=False)

    class Meta:
        model = Order
        fields = ['status', 'courier']
