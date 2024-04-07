from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

 
from restaurant.validators import validate_ifsc_code
from .models import Document
from .validators import validate_license_no, validate_pancard_no


 


class DocumentForm(forms.Form):
    license_number = forms.CharField(label='Driving Licence Number', validators=[validate_license_no],
                                     help_text="Enter 16 character Licenese number. e.g. HR-0619850034761")
    license_document = forms.ImageField(label='Driving Licence', help_text="Upload Front Image of Driving Licence")
    pancard_number = forms.CharField(label='PanCard Number', validators=[validate_pancard_no],
                                     help_text="Enter 10 digit PAN card number.  e.g. BNZAA2318J")
    pancard_document = forms.ImageField(label='PanCard', help_text="Upload Front Image of Pan card")
    account_no = forms.CharField(label="Bank Account Number", help_text='Enter 8 to 18 digit bank account number',
                                 validators=[MinLengthValidator(8), MaxLengthValidator(18)], max_length=18)
    ifsc_code = forms.CharField(label="IFSC Code", max_length=11, help_text='Enter 11 digit bank\'s IFSC Code',
                                validators=[validate_ifsc_code])

    def save(self, **kwargs):
        agent = kwargs['agent']
        return Document.objects.create(agent=agent, **self.cleaned_data)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line1', 'address_line2', 'street', 'landmark', 'pincode', 'city', 'state']

    def save(self, **kwargs):
        address = Address.objects.create(address_title=DELIVERY_AGENT_ADDRESS_TITLE, **self.cleaned_data)
        user = kwargs['agent']
        user.addresses.add(address)
        return address

    def clean(self):
        super(AddressForm, self).clean()

        # validate pin code
        pin_code = self.cleaned_data.get('pincode')
        if len(str(pin_code)) != 6:
            self.add_error('pincode', "Invalid pincode")
 