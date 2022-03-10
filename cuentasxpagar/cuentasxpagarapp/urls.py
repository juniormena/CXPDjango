
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('proveedores/', views.proveedores),
    path('registrarproveedor/', views.registrarproveedor),
    path('edicionprove/<int:codigo>', views.edicionProve),
    path('editarprove/<int:codigo>/', views.editarProve),
    path('eliminarProve/<int:codigo>', views.eliminarProve),
    
    #EntradaDocumentos urls
    path('entradaDocumentos/', views.entradaDocumentos),
    path('addEntradaDocumento/', views.addEntradaDocumento),
    path('editEntradaDocumento/<int:codigoEntradaDocumento>/', views.editEntradaDocumento),
    path('deleteEntradaDocumento/<int:codigoEntradaDocumento>', views.deleteEntradaDocumento),
    
]
