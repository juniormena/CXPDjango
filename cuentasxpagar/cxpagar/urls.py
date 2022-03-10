from django.urls import path
from . import views

urlpatterns = [
    path('conceptos', views.conceptos, name='conceptos'),
    path('conceptos/crear', views.crear_concepto, name='crear_con'),
    path('conceptos/editar', views.editar_concepto, name='editar_con'),
]