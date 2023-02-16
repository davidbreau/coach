from django import forms
from django.forms import DateInput

class DatePickerInput(DateInput):
    template_name = 'coachapp/app/templates/app/datepicker.html'

# class DatePickerInput(forms.DateInput):
#     input_type = 'date'

# class TimePickerInput(forms.TimeInput):
#     input_type = 'time'

# class DateTimePickerInput(forms.DateTimeInput):
#     input_type = 'datetime'