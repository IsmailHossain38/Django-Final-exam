
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.UserLogin.as_view() , name='login'),
    path('register/',views.register , name='register'),
    path('profile/',views.Profile.as_view(), name='profile'),
    path('profile/Personalupdate/', views.userPersonalUpdate, name='updateview' ),
    path('profile/pass_change/', views.pass_change, name='password_change' ),
    path('logout/', views.Userlogout , name ='logout'),
    path('applyfortution/<int:id>/', views.applyfortution, name='applyfortution'),
    path('active/<uid64>/<token>/', views.activate,name='active'),
]
 
 