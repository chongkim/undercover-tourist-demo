from django.db import models

class ProductListing(models.Model):
    name = models.TextField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    slug = models.TextField(max_length=255)
    uuid = models.TextField(max_length=255)

class Purchase(models.Model):
    confirmation_code = models.TextField(max_length=20)
    product_name = models.TextField(max_length=255)
    product_price = models.DecimalField(decimal_places=2, max_digits=20)
    product_cost = models.DecimalField(decimal_places=2, max_digits=20)
    quantity = models.IntegerField()
    customer_name = models.TextField(max_length=255)
    customer_email = models.EmailField(max_length=255)
    customer_phone = models.TextField(max_length=255)
