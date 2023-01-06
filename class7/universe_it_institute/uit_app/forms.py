from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Name"
    }))
    email =forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control'
    }))
    class Meta:
        model = ContactUs
        fields = '__all__'
        # fields = ['name','email', 'subject', 'message']

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'