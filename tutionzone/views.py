from tution.models import AddTutors
from categorybyclasses.models import CategoryByClasses
from django.shortcuts import render

def home(request ,Category_slug =None):
    data = AddTutors.objects.all()
    form = CategoryByClasses.objects.all()
    if Category_slug is not None:
        class_category = CategoryByClasses.objects.get(slug = Category_slug)
        data = AddTutors.objects.filter(class_category=class_category)
    return render(request, 'home.html',{'data':data , 'category':form})