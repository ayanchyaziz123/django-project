from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Contact


class Contact(UserCreationForm):
    Email = forms.EmailField(max_length=60, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder' : 'email'
        }
    ))
    Name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'user name'
        }
    ))
    Content = forms.CharField( widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))



    class Meta:
        model = Contact
        fields = ("Email", "Name", "Content")


