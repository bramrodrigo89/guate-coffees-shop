from django.contrib import admin
from .models import Product, Region, ProductImage

# Register your models here.

#class ProductImagesAdmin(admin.TabularInline):

class ProductImagesAdmin(admin.ModelAdmin):
    #model = ProductImage
    #extra = 4
    list_display = (
        'image',
        'product'
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'region',
        'name',
        'description',
        'description_2',
        'finca',
        'roast_level',
        'cupping_notes',
        'retail_price',
        'new_product',
        'rating',
        'main_image',
        'other_images'
    )
    #inlines = [ProductImagesAdmin,]
    ordering = ('region',)

class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'description',
        'weather_temperature',
        'precipitation',
        'humidity',
        'altitude'
    )
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(ProductImage, ProductImagesAdmin)