from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse

PRODUCT_CATEGORY = (("CLOTHES", "Одежда"), ("TECH", "Техника"), ("SERVICE", "Услуги"))

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORY, default="CLOTHES")
    description = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to="pictures/", default="static/images/images.png",
                              null=True, blank=True)

    def get_absolute_url(self):
        return reverse('webapp:product_list_view')


class Review(models.Model):
    author = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    evaluation = models.PositiveIntegerField(validators=(MaxValueValidator(5,),))
    is_moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
