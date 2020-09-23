from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from star_ratings.models import Rating


class Region(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)
    description = models.TextField()
    weather_temperature = models.CharField(max_length=100)
    precipitation = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    altitude = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    region = models.ForeignKey(
        'Region', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(default='', null=False, blank=False)
    description_2 = models.TextField(default='', null=False, blank=False)
    finca = models.CharField(max_length=30, null=True, blank=True)
    roast_level = models.CharField(max_length=30, default='')
    cupping_notes = models.CharField(max_length=100, null=True, blank=True)
    retail_price = models.DecimalField(
        max_digits=5, decimal_places=2, default=15.00)
    new_product = models.BooleanField(default=False)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, default=5.00, null=True, blank=True)
    ratings = GenericRelation(Rating, related_query_name='products')
    main_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product', related_name='other_images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'Image for product: {self.product.name}'


class ProductReview(models.Model):
    product = models.ForeignKey(
        'Product', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
      User, on_delete=models.SET_NULL, null=True,
      blank=True, related_name='reviews')
    ratings = GenericRelation(Rating, related_query_name='product_review')
    description = models.TextField(
        default='Tell us your comments about this product')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review from {self.user} for product: {self.product.name}'
