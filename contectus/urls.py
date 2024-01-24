
from django.urls import path
from . import views
urlpatterns = [
    path('contect_us/',views.contactus , name='contect_us'),
]
 