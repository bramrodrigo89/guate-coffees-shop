from django.db import models

class Region(models.Model):
    region_id = models.Charfield
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=False, blank=False)
    description	= models.CharField(max_length=600, null=False, blank=False)
    weather_temperature	= models.CharField(max_length=100, null=False, blank=False)
    precipitation = models.CharField(max_length=100, null=False, blank=False)
    humidity = models.CharField(max_length=100, null=False, blank=False)
    altitute = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class Product(models.Model):
    region = models.ForeignKey('Region', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    region
    product_category
    name
    description
    description_2
    finca
    roast_level
    cupping_notes
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)
    new_product
    images
    
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.name

