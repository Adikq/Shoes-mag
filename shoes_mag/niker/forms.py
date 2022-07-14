from django import forms

from .models import *


class OrderForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Order
        fields = ('name', 'number', 'address')

