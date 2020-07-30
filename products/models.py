from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)
    description	= models.TextField()
    weather_temperature	= models.CharField(max_length=100)
    precipitation = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    altitude = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    description_2 = models.TextField()
    finca = models.CharField(max_length=30, null=True, blank=True)
    roast_level = models.CharField(max_length=30)
    cupping_notes = models.CharField(max_length=100, null=True, blank=True)
    retail_price = models.DecimalField(max_digits=5, decimal_places=2)
    new_product = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='other_images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'Image for product: {self.product.name}'

