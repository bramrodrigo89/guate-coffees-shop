from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number',
                  'street_address_1', 'street_address_2',
                  'town_or_city', 'state', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'first_name': 'Example: John',
            'last_name': 'Example: Smith',
            'email': 'your_email@mail.com',
            'phone_number': '(123) 456 - 7890',
            'postcode': 'ZIP',
            'town_or_city': 'Town or City',
            'street_address_1': 'Number, Street Name',
            'street_address_2': 'Apartment Number, PO BOx',
            'state': 'Example: CA',
        }

        self.fields['username'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'