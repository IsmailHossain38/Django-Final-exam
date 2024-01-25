
from django.urls import path
from . import views
urlpatterns = [

   path('details/<int:id>/',views.tutorDetails, name='details'),
   path('about_us/',views.about_us, name='about_us'),
   path('find_tutor/',views.find_tutor, name='find_tutor'),
   path('review/<int:id>/',views.TutorDetails.as_view() , name='review'),
]
