from django.urls import path
from . import views

urlpatterns = [
     path('',views.register,name='register'),
     path('login/',views.user_login,name='login'),
     path('logout/',views.user_logout,name='logout'),
     path('profile/',views.profile,name='profile'),
     path('profile/edit/',views.edit_profile,name='editprofile'),
     path('profile/edit/passchange',views.pass_change,name='passchange'),
     path('profile/edit/passchange2',views.passchange_without,name='passchange2'),


]

