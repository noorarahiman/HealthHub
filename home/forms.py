from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__',

        
        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'form-control'}),
            'p_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'p_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'doc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'booking_date': DateInput(attrs={'class': 'form-control'}),
        }

        
        labels = {
            'p_name': "Patient Name:",
            'p_phone': "Patient Phone:",
            'p_email': "Patient Email:",
            'doc_name': "Doctor Name:",
            'booking_date': "Booking Date:",
        }