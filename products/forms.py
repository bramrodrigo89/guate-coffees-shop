from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Region


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # image = forms.ImageField(
    #     label='Main Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        regions = Region.objects.all()
        #creates a list of touples of friendly names with 
        # their associated id's for every category
        friendly_names = [(r.id, r.get_friendly_name()) for r in regions]

        self.fields['region'].choices = friendly_names
