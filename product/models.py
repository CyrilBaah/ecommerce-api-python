from django.db import models

from category.models import Category


# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    featured = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name
