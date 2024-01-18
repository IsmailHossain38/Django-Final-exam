
from django.urls import path
from . import views
urlpatterns = [

   path('details/<int:id>/',views.tutorDetails, name='details'),
   path('review/<int:id>/',views.TutorDetails.as_view() , name='review'),
]
