
from . import views
from cuentasxpagarapp.loginViews import loginViews
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #authentication urls
    path('login/', loginViews.signIn, name='login'),
    path('logout/', loginViews.signOut, name='logout'),
    
    #Home url
    path('', views.home, name='home'),
    
     #Proveedores urls
    path('proveedores/', views.proveedores),
    path('registrarproveedor/', views.registrarproveedor),
    path('edicionprove/<int:codigo>', views.edicionProve),
    path('editarprove/<int:codigo>/', views.editarProve),
    path('eliminarProve/<int:codigo>', views.eliminarProve),
    
    #Conceptos urls
    path('conceptos/', views.conceptos),
    path('addConcepto/', views.addConcepto),
    path('editConcepto/<int:codigoConcepto>/', views.editConcepto),
    path('deleteConcepto/<int:codigoConcepto>', views.deleteConcepto),
    
    #EntradaDocumentos urls
    path('entradaDocumentos/', views.entradaDocumentos),
    path('addEntradaDocumento/', views.addEntradaDocumento),
    path('crearAsiento/', views.crearAsiento),
    path('noData/', views.noData),
    path('editEntradaDocumento/<int:codigoEntradaDocumento>/', views.editEntradaDocumento),
    path('deleteEntradaDocumento/<int:codigoEntradaDocumento>', views.deleteEntradaDocumento),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
