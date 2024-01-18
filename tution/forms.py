from django import forms 
from .models import AddTutors ,Review
class AddTutorForm(forms.ModelForm):
    class Meta:
        model =AddTutors
        fields ="__all__"
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =['name','email','rating','body']