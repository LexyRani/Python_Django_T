from .views import ProductListView
from .views import ProductCreateView
from .views import ProductUpdateView
from .views import ProductDeleteView
from .views import ProductDetailView
from .views import InvoiceDetailView
from .views import InvoiceListView
from .views import invoice_create
from django.views.generic import RedirectView
from django.urls import path
from django.urls import reverse_lazy

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('product-list')), name='home'),
    path("products/",ProductListView.as_view(), name="product-list"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("products/<int:pk>/detail/", ProductDetailView.as_view(), name ="product-detail"),
    path("invoices/", InvoiceListView.as_view(), name="invoice-list"),
    path("invoices/create/", invoice_create, name="invoice-create"),
    path("invoices/<int:pk>/detail/", InvoiceDetailView.as_view(), name="invoice-detail"),
]