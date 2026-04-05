from .views import ProductListView
from .views import ProductCreateView
from .views import ProductUpdateView
from .views import ProductDeleteView
from django.urls import path

urlpatterns = [
    path("products/",ProductListView.as_view(), name="product-list"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
]