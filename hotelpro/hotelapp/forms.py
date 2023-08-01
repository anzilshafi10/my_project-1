from django import forms
from . models import Booking
from . models import Comment

class TodoForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets={
            'date':DateInput()
        }



