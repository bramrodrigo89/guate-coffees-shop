from django import forms
from .models import UserInfo, UserDeliveryInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, add custom labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Example: John',
            'last_name': 'Example: Smith',
            'email': 'youremail@email.com',         
        }
        labels = {
            'first_name': 'First Name, Middle Name',
            'last_name': 'Last Name',
            'email': 'Email Address',           
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-info-input'


class UserDeliveryInfoForm(forms.ModelForm):
    class Meta:
        model = UserDeliveryInfo
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, add custom labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': '+1 (123) 456 - 7890',
            'default_street_address_1': 'Number, Street Name',
            'default_street_address_2': 'Apartment Number, PO BOx',
            'default_town_or_city': 'Town or City',
            'default_state': 'Example: CA',
            'default_postcode': 'ZIP',            
        }
        labels = {
            'default_phone_number': 'Phone Number',
            'default_street_address_1': 'Address Line 1',
            'default_street_address_2': 'Address Line 2',
            'default_town_or_city': 'Town or City',
            'default_state': 'State',
            'default_country': 'Country',
            'default_postcode': 'Postal Code',            
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'




