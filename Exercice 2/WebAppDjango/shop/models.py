from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name


class Invoice(models.Model):
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Facture #{self.id}"

    def total_products(self):
        return sum(item.quantity for item in self.invoiceitem_set.all())

    def total_price(self):
        return sum(item.line_total() for item in self.invoiceitem_set.all())


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    def line_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"