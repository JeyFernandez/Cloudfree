from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manuales/', views.all_manuals, name='all_manuals'),
    path('manual/<slug:slug>/', views.manual_detail, name='manual_detail'),
]