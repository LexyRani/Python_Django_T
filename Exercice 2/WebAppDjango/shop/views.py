from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product, Invoice
from .forms import ProductForm, InvoiceForm, InvoiceItemFormSet


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 5


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_delete.html'
    success_url = reverse_lazy('product-list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'shop/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 10
    ordering = ['-id']


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            formset = InvoiceItemFormSet(request.POST, instance=invoice)

            if formset.is_valid():
                items = formset.save(commit=False)

                for item in items:
                    if item.product and item.quantity and item.unit_price:
                        item.invoice = invoice
                        item.save()

                return redirect('invoice-detail', pk=invoice.pk)
            else:
                invoice.delete()
    else:
        form = InvoiceForm()
        formset = InvoiceItemFormSet()

    return render(request, 'shop/invoice_form.html', {
        'form': form,
        'formset': formset,
    })


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'shop/invoice_detail.html'
    context_object_name = 'invoice'