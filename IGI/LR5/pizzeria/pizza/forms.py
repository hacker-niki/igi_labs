# pizza/forms.py

from django import forms

from .models import Pizza, Order, PromoCode


class PizzaFilterForm(forms.Form):
    max_price = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    category = forms.ModelChoiceField(queryset=Pizza.objects.all(), required=False)
    SORT_CHOICES = [
        ('price_asc', 'Цена по возрастанию'),
        ('price_desc', 'Цена по убыванию'),
    ]
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False)
    sauce_search = forms.CharField(max_length=100, required=False, label='Поиск по соусу', initial="")


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'sauce', 'price', 'category']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizza', 'quantity', 'courier']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courier'].required = False  # Make courier optional for the client


class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code', 'discount', 'is_active']
