from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date']  # all editable fields

        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'form-control'}),
            'p_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'p_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'doc_name': forms.Select(attrs={'class': 'form-control'}),  # dropdown for ForeignKey
            'booking_date': DateInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'p_name': "Patient Name:",
            'p_phone': "Patient Phone:",
            'p_email': "Patient Email:",
            'doc_name': "Doctor Name:",
            'booking_date': "Booking Date:",
        }