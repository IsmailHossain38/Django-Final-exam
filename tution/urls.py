
from django.urls import path
from . import views
urlpatterns = [

   path('details/<int:id>/',views.tutorDetails, name='details'),
   path('about_us/',views.about_us, name='about_us'),
   path('review/<int:id>/',views.TutorDetails.as_view() , name='review'),
]
