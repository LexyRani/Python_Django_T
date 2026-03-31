from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    expiration_date = models.DateField()


class Invoice(models.Model):
    created_at=models.DateField()
    

class InvoiceItem(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price= models.DecimalField(max_digits=8, decimal_places=2)