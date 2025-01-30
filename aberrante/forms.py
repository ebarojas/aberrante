from django import forms
from .models import Lead

class SimpleForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['email']
