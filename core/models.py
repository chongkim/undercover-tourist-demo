from django.db import models

class ProductListing(models.Model):
    name = models.TextField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    slug = models.TextField(max_length=255)
    uuid = models.TextField(max_length=255)