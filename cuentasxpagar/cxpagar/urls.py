from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('conceptos', views.conceptos, name='conceptos'),
]