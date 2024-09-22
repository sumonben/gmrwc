from django.contrib import admin
from django.urls import path,include, re_path
from frontpage import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.frontpage_view.as_view(), name='home'),
    path('showpage/<str:navitem_name>/<str:navelement_head>/<str:heading>/<str:id>', views.showPage, name="showpage"),

]