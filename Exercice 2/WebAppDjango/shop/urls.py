from .views import ProductListView
from .views import ProductCreateView
from django.urls import path

urlpatterns = [
    path("products/",ProductListView.as_view(), name="product-list"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
]