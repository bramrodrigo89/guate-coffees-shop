from django import forms
from .models import CustomerInquiry


class CustomerInquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and labels, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': '',
            'first_name': 'Example: John',
            'last_name': 'Example: Smith',
            'email': 'your_email@mail.com',
            'phone_number': '+1 (123) 456 - 7890',
            'user': 'Username',
            'description': 'What would you like to say?',
            'created_at': 'Date of creation',
        }
        labels = {
            'category': '',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'user': 'Username',
            'description': 'Your Inquiry',
            'created_at': 'Date',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['category'].widget = forms.HiddenInput()
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
