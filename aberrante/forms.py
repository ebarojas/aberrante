from django import forms
from .models import Lead

class SimpleForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'gabriel@aol.com'}),
        }

class LeadTypeForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['email', 'type']
        # Define Label
        labels = {
            "email": "email",
            "type": "¿Qué eres?",
        }
        # Define a place holder
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'gabriel@aol.com'}),
        }
