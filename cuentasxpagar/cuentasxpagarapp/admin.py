from django.contrib import admin
from cuentasxpagarapp.models import Proveedor, EntradaDocumento, Concepto
# Register your models here.
admin.site.register(Proveedor)
admin.site.register(EntradaDocumento)
admin.site.register(Concepto)