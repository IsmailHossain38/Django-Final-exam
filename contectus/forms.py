from django import forms 
from .models import ContectUsModel
class ContectUsForm(forms.ModelForm):
    class Meta:
        model = ContectUsModel
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name '}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email '}),
            'Number': forms.TextInput(attrs={'placeholder': 'Enter your number'}),
            'body': forms.Textarea(attrs={'placeholder': 'Tell us about yourself'}),
            
        }