from django.contrib import admin
from django.urls import path,include, re_path
from frontpage import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.frontpage_view.as_view(), name='home'),
    path('language_change/', views.languageChange, name='language_change'),
    path('showpage/<str:navitem_name>/<str:navelement_head>/<str:heading>/<str:id>', views.showPage, name="showpage"),
    path('showpage_service_box_item/<int:servicebox_id>/<str:servicebox_title>/<str:heading>/<str:id>', views.showServiceBoxItem, name="showpage_servicebox_item"),


]