from . import forms 
from .models import CategoryByClasses

class CategoryForm(forms.Modelform):
    class Meta:
        model =CategoryByClasses
        fields="__all__"