from django.contrib import admin
from django.urls import path,include, re_path
from frontpage import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    
    path('', cache_page(60 * 60)(views.frontpage_view.as_view()), name='home'),
    path('language_change/', views.languageChange, name='language_change'),
    path('showpage/<str:navitem_name>/<str:navelement_head>/<str:heading>/<str:id>/', views.showPage, name="showpage"),
    path('showpage_service_box_item/<int:servicebox_id>/<str:servicebox_title>/<str:heading>/<str:id>/', views.showServiceBoxItem, name="showpage_servicebox_item"),
    path('tableshow/<str:tableall>/', views.tableAllShow, name="tableshow"),
    path('single-notice/<int:id>/', views.singleNotice, name="single_notice"),

    path('testhtml/', views.testHtml, name="testhtml"),



]