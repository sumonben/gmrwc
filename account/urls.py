from django.contrib import admin
from django.urls import path,include, re_path
from . import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('/login',views.Login, name='login'),
    path('/register',views.Registration, name='register'),
    path('/profile',views.Profile, name='profile'),
    path('/logout', views.Logout, name='logout'),

]