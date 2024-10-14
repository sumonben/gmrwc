from django.contrib import admin
from django.urls import path,include, re_path
from . import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('/student', views.testHtml, name="student"),



]