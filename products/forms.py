from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Region, ProductImage, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    main_image = forms.ImageField(
            label='Main Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        
        """
        Add placeholders, add custom labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Product Name - Brand - Producer',
            'region':'Region name',
            'description': 'Enter general description',
            'description_2': 'Add product origin description, history, other details...',
            'finca': 'e.g. La Hermosa',
            'roast_level': 'e.g. dark, medium, light',
            'cupping_notes': 'chocolate, cherry, nuts...',
            'retail_price':'Price in US$',
            'rating':'Rating from 1 to 5',
            'main_image': 'Shown in in search results',
            'new_product': 'Is this product new?',
        }
        labels = {
            'name': 'Product Name',
            'region':'Origin Region',
            'description': 'Main Description',
            'description_2': 'Secondary Description',
            'finca': 'Finca Name',
            'roast_level': 'Roast Level',
            'cupping_notes': 'Cupping Notes',
            'retail_price':'Price In US$',
            'rating':'Customer Rating (1 to 5)',
            'main_image': 'Main Image',
            'new_product': 'Feature As New Product',
        }
        

        regions = Region.objects.all()
        #   creates a list of touples of friendly names with their IDs
        friendly_names = [(r.id, r.get_friendly_name()) for r in regions]
        self.fields['region'].choices = friendly_names

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label
            
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            

class AdditionalImage(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ['user']