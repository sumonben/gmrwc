from django.contrib import admin
from django.urls import path,include, re_path
from . import views
import static
from django.conf import settings
from django.conf.urls.static import static
from django import views as django_views

urlpatterns = [
    path('/student', views.testHtml, name="student"),
    path('/certificate/<int:id>/<str:type>', views.certificateGenerate, name="certificate"),
    path('/get-certificate', views.getCertificate, name="get-certificate"),

    path('/jsi18n', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),



]