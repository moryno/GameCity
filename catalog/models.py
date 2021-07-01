from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Category(models.Model):
    name = models.CharField(
        max_length=255, help_text='Enter a category here')
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this category."""
        # return reverse('category-detail', args=[str(self.id)])
        return reverse('catalog:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """Model representing a product class."""
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(
        max_length=255, help_text='Enter a product name')
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(
        max_length=1000, blank=True, help_text='Enter a brief description of the product')
    price_in_shillings = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    condition = models.CharField(
        max_length=255, null=True, blank=True)
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['name']
        # we define this index because we want to query products by both id and slug
        index_together = ('id', 'slug')
        verbose_name_plural = "products"

    @property
    def is_available(self):
        if self.available and date.today() > self.available:
            return True
        return False

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this electronic."""
        # return reverse('product-detail', args=[str(self.id)])
        return reverse('catalog:product_detail', args=[self.id, self.slug])


