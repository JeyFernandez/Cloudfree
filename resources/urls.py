from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('recursos/', views.resource_list, name='resource_list'),
    path('recursos/<slug:slug>/', views.resource_detail, name='resource_detail'),
]
