from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Region


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        regions = Region.objects.all()
        friendly_names = [(r.id, r.get_friendly_name()) for r in regions]

        self.fields['region'].choices = friendly_names
