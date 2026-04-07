from django import forms
from django.forms import inlineformset_factory
from .models import Product, Invoice, InvoiceItem


class ProductSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value and hasattr(value, "instance"):
            option["attrs"]["data-price"] = value.instance.price
        return option


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'product': ProductSelect(),
            'quantity': forms.NumberInput(attrs={'min': 1}),
            'unit_price': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }


InvoiceItemFormSet = inlineformset_factory(
    Invoice,
    InvoiceItem,
    form=InvoiceItemForm,
    extra=3,
    can_delete=False
)