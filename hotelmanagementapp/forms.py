from django import forms
from . models import Booking, RoomType

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'phone_number', 'check_in_date', 'check_out_date','room_type']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'check_in_date':forms.DateInput(attrs={'type': 'date'}),
            'check_out_date':forms.DateInput(attrs={'type': 'date'}),
            'room_type':forms.Select(attrs={'class': 'form-select'})

        }
        