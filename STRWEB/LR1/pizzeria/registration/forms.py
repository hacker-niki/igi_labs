import re
from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Customer


def validate_phone_number(value):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    if not pattern.match(value):
        raise ValidationError('Номер телефона должен быть введен в формате: "+999999999". До 15 цифр.')


def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError('Вы должны быть старше 18 лет для регистрации.')


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), validators=[validate_age])
    phone_number = forms.CharField(validators=[validate_phone_number])

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1",
                  "password2", "date_of_birth", "phone_number")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            customer = Customer(
                user=user,
                date_of_birth=self.cleaned_data["date_of_birth"],
                telephone_number=self.cleaned_data["phone_number"]
            )
            customer.save()
        return user
