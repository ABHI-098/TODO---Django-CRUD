from django.core import validators

from django import forms

from .models import User

class TaskFeed(forms.ModelForm):
    class Meta:
        model = User
        fields =['title','description','priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' }),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.TextInput (attrs={'class': 'form-control' }),            
            }