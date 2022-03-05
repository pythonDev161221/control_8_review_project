from django.db import models

# Create your models here.
PRODUCT_CATEGORY = (("CLOTHES", "Одежда"), ("TECH", "Техника"), ("SERVICE", "Услуги"))


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORY, default="CLOTHES")
    description = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to="pictures/", null=True, blank=True)
