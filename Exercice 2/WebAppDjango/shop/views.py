from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 5

class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop/product_form.html'
    fields = ['name', 'price', 'expiration_date']
    success_url = reverse_lazy('product-list')


   