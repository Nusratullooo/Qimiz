from home.models import ContactMessage
from product.models import Order
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'surname',  'phone',  'email', 'message')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'surname', 'phone', 'amount', 'category', 'food', 'address')
