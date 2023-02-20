# authentication/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Appointment


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff')

class DateInput(forms.DateInput):
    input_type = 'date'

class DateInput(forms.DateInput):
    input_type = 'date'
    
class AppointForm(forms.Form):
    name = forms.CharField()
    time = forms.ChoiceField(choices=Appointment.TIME_CHOICES)
    date = forms.DateField(widget=DateInput)
    message = forms.CharField(widget=forms.Textarea)
    # class Meta:
    #     model = Appointment
    #     fields = ('date', 'time','message')
    #     widgets = {
    #         'date': forms.DateInput(),
    #         'message': forms.Textarea()
    #     }

    # date = forms.DateField(widget=DateInput)
    # time = forms.ChoiceField(choices=[Appointment.TIME_CHOICES])
    # message = forms.CharField(widget=forms.Textarea)