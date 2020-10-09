from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Region, ProductImage, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        
        """All fields for this form."""
        model = Product
        fields = '__all__'

    main_image = forms.ImageField(
        label='Main Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """

        Add custom placeholders, custom labels and
        set autofocus on first field 'name'.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Product Name - Brand - Producer',
            'region': 'Region name',
            'description': 'Enter general description',
            'description_2': 'Describe product origin, history, etc',
            'finca': 'e.g. La Hermosa',
            'roast_level': 'e.g. dark, medium, light',
            'cupping_notes': 'chocolate, cherry, nuts...',
            'retail_price': 'Price in US$',
            'rating': 'Rating from 1 to 5',
            'main_image': 'Shown in in search results',
            'new_product': 'Is this product new?',
        }
        labels = {
            'name': 'Product Name',
            'region': 'Origin Region',
            'description': 'Main Description',
            'description_2': 'Secondary Description',
            'finca': 'Finca Name',
            'roast_level': 'Roast Level',
            'cupping_notes': 'Cupping Notes',
            'retail_price': 'Price In US$',
            'rating': 'Customer Rating (1 to 5)',
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


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """

        Add custom placeholders, custom labels and
        make star_percentage and user_rating hidden fields.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user': 'Your username',
            'product': 'Product to be reviewed',
            'user_rating': 'From 1 to 5',
            'star_percentage': 'This is calculated automatically',
            'description': 'How was your experience with this product?',
            'created_at': '', 'updated_at':
            ''
        }
        labels = {
            'user': '',
            'product': 'Product Name',
            'user_rating': '',
            'star_percentage': '',
            'description': 'Your comments about this product:',
            'created_at': 'Created',
            'updated_at': 'Last Update'
        }

        for field in self.fields:
            label = labels[field]
            placeholder = placeholders[field]
            self.fields[field].label = label
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields['star_percentage'].widget = forms.HiddenInput()
        self.fields['user_rating'].widget = forms.HiddenInput()


class AdditionalImage(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'
