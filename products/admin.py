from django.contrib import admin
from .models import Product, Region, ProductImage

# Register your models here.


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImage
    extra = 4


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
        'main_image',
        'rating',
    )
    inlines = [ProductImagesAdmin, ]
    ordering = ('pk',)


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
