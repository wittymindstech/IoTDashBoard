from django.forms import ModelForm
from django import forms

class UserRegistrationForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})
    )
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget= forms.TextInput(attrs={'class': 'form-control' ,  'placeholder': 'Enter Username'})

    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
